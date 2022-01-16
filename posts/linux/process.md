---
title: 프로세스에 대해 알아보자
date: 2022-01-15 21:13:50 +09:00
---
---

## fork()

```c
#include <unistd.h>
pid_t fork()
"현재 프로세스에서 자식 프로세스를 복제"
```

현재 실행중인 프로세스의

반환값은
- 부모 프로세스: 자식 프로세스의 pid
- 자식 프로세스: 0

그러니

## waitpid()

1. fork()


```c
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(void) {
  pid_t pid;

  pid = fork();
  if (pid == 0) {
    printf("[자식 프로세스] 내 pid:%d\n", getpid());
    sleep(3);
    printf("[자식 프로세스] ok i'm die thank you forever\n");
  } else if (pid > 0) {
    printf("[부모 프로세스] 자식 프로세스 pid는:%d\n", pid);
    waitpid(pid, NULL, 0);
    printf("[부모 프로세스] 자식 프로세스 %d가 끝남\n", pid);
  }
  return (0);
}
```

[fork()](https://codetravel.tistory.com/23)