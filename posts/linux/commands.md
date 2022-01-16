---
title: 리눅스 명령어 이모저모
date: 2022-01-15 13:16:08 +09:00
---

## `ln` 순서 헷갈릴 때 보기

```bash
ln -s "원본파일" "링크"
```

- `cp`, `mv` 명령어와 **원본**과 **목적지**의 순서가 같다
- 원본 파일을 가리키는 링크를 만든다
- 실수로 원본과 목적지를 반대로 적어 실행하면 이미 파일이 있다는 오류가 뜬다. 이때 `-f` 명령어로 강제로 실행하면 덮어씌워지니 쓰면 안 된다.


## `rm` 안전하게 쓰기

rm은 위험하다. 평소에 조심해서 쓴다 해도

- `rm ~`나
- `rm / $HOME/a/b/c`

같은 실수를 무심결에 할 수 있다. 이때 `rm`의 사용을 막거나 `alias rm=trash`등 안전한 명령어로 바꾸어 놓으면 실수로 중요한 파일을 지우더라도 복구할 수 있다.

- [trash-cli:삭제시 파일을 휴지통으로 옮긴다](https://github.com/sindresorhus/trash-cli)
- [safe-rm: rm이 적용되지 않는 디렉토리 목록을 정할 수 있다.](https://github.com/kaelzhang/shell-safe-rm)

[안전하게 rm 하는 법](https://github.com/sindresorhus/guides/blob/main/how-not-to-rm-yourself.md#safeguard-rm)

## `apt`? `apt-get`?

[it's foss](https://itsfoss.com/apt-vs-apt-get-difference/)

- `apt`

  - 일반 사용자용
  - 간략한 명령어 옵션
  - 로딩 바, 패키지 목록등 편의성 기능

- `apt-get`
  - 고급 사용자 및 스크립팅용
  - 다양한 명령어 옵션
