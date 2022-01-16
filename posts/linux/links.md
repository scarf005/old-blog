---
title: 하드 링크 vs 심볼릭 링크 vs cp
date: 2022-01-16 21:52:11 +09:00
---

## 하드 링크 vs 심볼릭 링크 vs 복사하기

리눅스의 파일들은 모든 파일들은 inode라고 하는 고유한 번호로 구분이 되는데, 파일들은 사실 이 번호를 가리키는 `바로가기`와 비슷하다. 예제를 통해 확인하면

```bash
❯ echo "asdf" > foo.txt

❯ cp foo.txt foo_copy.txt
❯ ln foo.txt foo_hard_link.txt
❯ ln -s foo.txt foo_sym_link.txt

❯ ls -i # inode값 확인. foo.txt와 foo_hard_link.txt의 inode가 같다.
11534802 foo.txt
11534803 foo_copy.txt
11534802 foo_hard_link.txt
11534804 foo_sym_link.txt ⇒ foo.txt

❯ echo "add" >> foo_hard_link.txt
❯ cat foo.txt # 하드 링크와 원본은 디스크의 같은 데이터를 가리킨다
asdf
add

❯ rm foo.txt
❯ cat foo_sym_link.txt
cat: foo_sym_link.txt: 그런 파일이나 디렉터리가 없습니다
❯ echo asdf > foo.txt
❯ cat foo_sym_link.txt # 심볼릭 링크는 inode값이 아닌 파일 경로에 대한 바로가기
asdf
```

<!--  -->