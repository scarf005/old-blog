---
title: pathlib 쓰는 법
date: 2022-01-02
---

## pathlib이란

- 경로를 `객체`처럼 다룰 수 있다

## 경로 다루기

```py
from pathlib import path

>>> from pathlib import Path
>>> p = Path()
>>> p
PosixPath('.')
>>> p = p / "디렉토리"
>>> p
PosixPath('디렉토리')
>>> p /= "파일"
>>> p
PosixPath('디렉토리/파일')
>>> p = p.with_suffix(".txt")
>>> p
PosixPath('디렉토리/파일.txt')
```

## `Path()` 객체에서 찾기

```py
>>> p.name
'파일.txt'
>>> p.parent
PosixPath('디렉토리')
>>> p.stem
'파일'
```

## 디렉토리에서 찾기
```py
❯ tree .
.
├── dir1
│   ├── c.txt
│   └── dir2
│       ├── a.txt
│       └── b.txt
├── dir3
│   └── d.txt
└── e.txt

>>> for f in Path().glob("**/*.txt"):
...     print(f)
e.txt

>>> for f in Path().glob("**/*.txt"):
...     print(f)
e.txt
dir1/c.txt
dir1/dir2/b.txt
dir1/dir2/a.txt
dir3/d.txt

>>> for f in Path().glob("*"):
...     print(f)
dir1
e.txt
dir3
```
