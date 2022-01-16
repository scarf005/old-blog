---
title: 파일 식별자(file descriptor) 완벽 이해하기
date: 2022-01-15 13:43:57 +09:00
---

## 3줄 요약

- 어떠한 **파일**을 가리키는 **바로가기**
- 파일은 파일 뿐만 아니라 디렉토리, 파이프 등 다양함
- 0은 `표준 입력`, 1은 `표준 출력`, 2는 `표준 오류`

## 파일 식별자를 알아보자

- `파일 디스크립터`, `파일 식별자`라고 하니까 설명을 아무리 읽어도 이해가 가지 않는다.
- 하지만 하는 일은 쉽게 생각해서 **바로가기**다.
- 물론 실제 바로가기와 _완전히 같지는 않다._ 차이는 나중에 알아보자.

수학귀신에서 어렵게 팩토리얼이라고 하지 않는다. **쾅**이라고 부른다. 마찬가지로 이제부터는 파일 식별자가 아니다. **바로가기**다.

프로그램이 실행되면 기본적으로 `바로가기` 3개를 가지게 된다.

- 0 -> 표준 입력
- 1 -> 표준 출력
- 2 -> 표준 오류

보통은 표준 입력에서 읽어와서 표준 출력이나 오류로 내보내게 된다.

### open

```c
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
int open(const char *pathname, int flags)
int open(const char *pathname, int flags, mode_t mode)
"파일을 (만들고) 열기"


```
- 파일을 열고(아니면 만들고) 그 파일을 가리키는 `바로가기`를 반환한다.

### read

```c
#include <unistd.h>
ssize_t read(int fd, void *buf, size_t count)
"바로가기가 가리키는 파일을 바이트로 읽기"

fd: 바로가기
buf: 읽은 바이트를 저장할 버퍼 포인터
count: 읽을 양
반환값: 읽은 바이트 수
```

```c
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main(void) {
  int 바로가기;
  char 읽은내용[8];

  // 읽기 전용 & 추가 모드로 파일 열기
  바로가기 = open("a.txt", O_RDWR | O_CREAT | O_APPEND, 0644);
  if (바로가기 < 0) {
    perror("파일 열던 중 오류 발생\n");
    exit(0);
  }
  for (int i = 0; i < 3; i++) {
    memset(읽은내용, 0, sizeof(읽은내용));
    read(바로가기, 읽은내용, sizeof(읽은내용));
    printf("[인덱스 %d] %s\n", i, 읽은내용);
  }
  close(바로가기);
}
```

예제 코드에서 변수 `바로가기`는 "a.txt"에 대한 바로가기를 담고 있다.

### dup

```c
int dup(int oldfd)

oldfd: 복사할 바로가기
반환값: 새로 만들어진 바로가기
```

`바로가기`를 복사해서 반환한다. 가령 `마인크래프트.exe` 게임의 바로가기 `마인크래프트 - 바로가기`가 있다고 해보자. 이 바로가기를 복사하면 어떻게 될까? 원
### dup2

## 참고자료

[inode](https://geek-university.com/linux/inode/)
[inode #2](https://rocksea.tistory.com/20)
[파일 테이블/파일 식별자 테이블](https://ehpub.co.kr/리눅스-시스템-프로그래밍-3-5-파일-테이블과-파일-디/)
[파일 디스크립터](https://www.computerhope.com/jargon/f/file-descriptor.htm)
[디렉토리도 파일인데 cat이 안 되는 이유](https://www.reddit.com/r/linuxquestions/comments/2tk2p1/if_everything_is_a_file_why_cant_i_do_cat/)
[ext4 파일시스템 구조](https://rrhh234cm.tistory.com/184)