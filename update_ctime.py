import fileinput
from datetime import datetime, timedelta, timezone
from pathlib import Path

# uses ctime but that's last inode change;
# changing filename, path etc will change that
# at least changing contents will not

tz = timezone(timedelta(hours=9))


def get_date(f: Path):
    ctime = datetime.fromtimestamp(f.stat().st_ctime, tz=tz)
    cal, tzstr = ctime.strftime("%Y-%m-%d %H:%M:%S"), ctime.strftime("%z")
    h, m = tzstr[:3], tzstr[3:]
    return f"{cal} {h}:{m}"


for f in Path("posts").glob("**/*.md"):
    lines = f.read_text().splitlines()
    if "date" not in lines[2]:
        lines[2] = f"date: {get_date(f)}\n---"
        f.write_text("\n".join(lines))
