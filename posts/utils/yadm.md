---
title: yadm으로 설정파일 동기화하기
date: 2022-01-08 23:20:56 +09:00
---

## yadm?

- [yadm](https://yadm.io/)은 `yet another dotfiles manager`의 약자
- 설정파일용 [git](https://git-scm.com/)
- [github](https://github.com/) 레포를 클론해서 다른 컴퓨터에서도 설정 목록을 내려받을 수 있다

## 사용법

[overview](https://yadm.io/docs/overview)

- git과 거의 비슷하게 동작한다
- 설정 파일을 따로 옮길 필요가 없다

처음에 이걸 몰라서 찾게 쉽게설정파일을 전부 한 곳에 몰아넣었는데, 굳이 그럴 이유가 없다. 앞으로는 심링크 방향을 반대로 해야 할듯?

```bash
yadm add ~/.zshrc
yadm clone github.com/scarf005/dotfiles
yadm status
```