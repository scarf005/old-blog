#!/usr/bin/env python3

from datetime import datetime, timedelta, timezone
from os import system
from pathlib import Path
from sys import argv

tz = timezone(timedelta(hours=9))


def get_date(f: Path):
    ctime = datetime.fromtimestamp(f.stat().st_ctime, tz=tz)
    cal, tzstr = ctime.strftime("%Y-%m-%d %H:%M:%S"), ctime.strftime("%z")
    h, m = tzstr[:3], tzstr[3:]
    return f"{cal} {h}:{m}"


def new_file(f: Path) -> Path:
    if f.exists():
        raise FileExistsError(f"{f} already exists")
    f.touch()
    f.write_text(f"---\ntitle: \ndate: {get_date(f)}\n---")
    return f


def rewrite_all(path: Path = Path("posts")):
    for f in path.glob("**/*.md"):
        lines = f.read_text().splitlines()
        if "date" not in lines[2]:
            lines[2] = f"date: {get_date(f)}\n---"
            f.write_text("\n".join(lines))


if __name__ == "__main__":
    if len(argv) == 3:
        category, name = argv[1:]
        new = (Path("posts") / category / name).with_suffix(".md")
        if not new.exists():
            new_file(new)
        system(f"code -r -g {new}:2:8")
    else:
        rewrite_all()
