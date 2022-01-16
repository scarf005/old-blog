---
title: 파일 식별자(file descriptor)란?
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

`바로가기`를 복사해서 반환한다. 가령 `마인크래프트.exe` 게임의 바로가기 `마인크래프트 - 바로가기`가 있다고 해보자. 이 바로가기를 복사하면 어떻게 될까? `마인크래프트.exe` 에는 변화가 없고 `마인크래프트 - 바로가기(2)`가 생길 것이다.

마찬가지로 `dup()`을 실행하면 oldfd `바로가기`를 복사해 새로운 `바로가기`를 반환한다. 이때 새 바로가기는 남는 번호중 가장 낮은 번호가 나온다. 어떤 이야기냐면 바로가기를 계속 만들면

- `마인크래프트 - 바로가기(3)`
- `마인크래프트 - 바로가기(4)`
- ...
  가 생기듯 4, 5, 6... 같은 식으로 다음에 남는 번호의 바로가기를 만들어 준다는 것이다.

```c
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main() {
  int foo바로가기 = open("foo.txt", O_CREAT | O_WRONLY | O_APPEND, 0644);
  int foo바로가기2 = dup(foo바로가기);

  printf("foo바로가기: %d, foo바로가기2: %d\n", foo바로가기, foo바로가기2);
  write(foo바로가기, "안녕 세상! ~ foo.txt - 바로가기\n", 41);
  write(foo바로가기2, "난 안녕 못한데 ~ foo.txt - 바로가기(2)\n", 50);
  close(foo바로가기);
  close(foo바로가기2);
  return 0;
}
❯ cat foo.txt
안녕 세상! ~ foo.txt - 바로가기
난 안녕 못한데 ~ foo.txt - 바로가기(2)
```

`foo바로가기`, `foo바로가기2` 모두 같은 `foo.txt` 파일을 가리키고 있다.

### dup2

```c
int dup2(int oldfd, int newfd)
"newfd가 가리키는 파일을 oldfd가 가리키는 파일로 바꾼다"
만약 newfd 바로가기가 이미 열려 있었으면 닫은 후 새로 열게 된다
반환값: newfd
```

#### 예제 1

```c
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main() {
  int bar바로가기 = open("bar.txt", O_CREAT | O_WRONLY | O_APPEND, 0644);
  int 반환값 = dup2(bar바로가기, STDOUT_FILENO);

	printf("반환값: %d, bar바로가기: %d\n", 반환값, bar바로가기);
  printf("HAYO!\n");
  return 0;
}
❯ ./"dup"
❯ cat bar.txt
반환값: 1, bar바로가기: 3
HAYO!
```

`printf`를 했는데 터미널에 출력이 뜨지 않고 `bar.txt`에 그 내용이 기록되었다. 어째서일까? 우선 `STDOUT_FILENO`는 `표준 출력 바로가기`와 같다. 지금까지

- bar바로가기 -> "bar.txt"
- 표준 출력 바로가기` -> 표준 출력

였다면 dup2로 표준 출력 바로가기가 가리키는 파일을 bar바로가기와 똑같이 바꿔줘서

- bar바로가기 -> "bar.txt"
- (좀 전까지)표준 출력 바로가기` -> "bar.txt"

가 된 것이다. printf는 `표준 출력 바로가기`가 가리키는 파일에 내용을 출력하는데 이건 이제 "bar.txt"를 가리키는 `바로가기`가 되었으니 "bar.txt"에 출력 내용이 써지게 된 것이다.

#### 예제 2

```c
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main() {
  int bar바로가기 = open("bar.txt", O_CREAT | O_WRONLY | O_APPEND, 0644);
  int spam바로가기 = open("spam.txt", O_CREAT | O_WRONLY | O_APPEND, 0644);
  int 반환값 = dup2(bar바로가기, spam바로가기);

  printf("반환값: %d, bar바로가기: %d, spam바로가기: %d\n", 반환값, bar바로가기,
         spam바로가기);
	write(bar바로가기, "애옹\n", 8);
  write(spam바로가기, "꿈틀꿈틀\n", 14);
  return 0;
}
❯ ./"dup"
반환값: 4, bar바로가기: 3, spam바로가기: 4
❯ cat bar.txt
애옹
꿈틀꿈틀
```

- bar바로가기 -> "bar.txt"
- spam바로가기 -> "spam.txt"

dup2로 spam바로가기가 bar바로가기와 같은 파일을 가리키게 바꾸면

- bar바로가기 -> "bar.txt"
- spam바로가기 -> "bar.txt"

## 참고자료

[inode](https://geek-university.com/linux/inode/)
[inode #2](https://rocksea.tistory.com/20)
[파일 테이블/파일 식별자 테이블](https://ehpub.co.kr/리눅스-시스템-프로그래밍-3-5-파일-테이블과-파일-디/)
[파일 디스크립터](https://www.computerhope.com/jargon/f/file-descriptor.htm)
[디렉토리도 파일인데 cat이 안 되는 이유](https://www.reddit.com/r/linuxquestions/comments/2tk2p1/if_everything_is_a_file_why_cant_i_do_cat/)
[ext4 파일시스템 구조](https://rrhh234cm.tistory.com/184)
