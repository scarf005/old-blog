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

# print("\n".join(lines))
# print(get_date(f))

# for post in Path("posts").glob("**/*.md"):
#     with post.opsen('r+') as f:
#         lines = f.readlines()
#         title = lines[0]
#         if "date" not in title:
#             lines[0] = title.replace("---", "---\ndate: 2020-01-01\n")
#         else:
#             lines[0] = title.replace("date: 2020-01-01", "date: 2020-01-01\n")
#     with open(post, "w") as f:
#         f.writelines(lines)
