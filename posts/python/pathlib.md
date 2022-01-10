---
title: pathlib 쓰는 법
---

## pathlib이란

- 경로를 `객체`로 다룰 수 있다
- [공식 문서](https://docs.python.org/ko/3/library/pathlib.html)

## 경로 다루기

```python
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

```python
>>> p.name
'파일.txt'
>>> p.parent
PosixPath('디렉토리')
>>> p.stem
'파일'
```

## 디렉토리에서 찾기
```python
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

## mv 쓰기
```python
>>> start = Path('somedir/a.txt')
>>> to = Path('./b.txt')
>>> start.rename(to)