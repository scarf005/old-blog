---
title: pthread가 뭔지 몰?루
date: 2022-01-15 21:18:46 +09:00
---

### 참고자료

[LLNL](https://hpc-tutorials.llnl.gov/posix/)
[man 3 pthread\_\*](https://linux.die.net/man/3/pthread_create)

## 스레드가 모지

|     종류     |                  특징                  |
| :----------: | :------------------------------------: |
| **프로그램** |        코드가 적힌 텍스트 파일         |
| **프로세스** |  메모리에 올라가 실행중인 _프로그램_   |
|  **스레드**  | *프로세스*에서 CPU가 처리중인 단위작업 |

pthread는 `Posix thread library`의 약자
[macos에서의 pthread.h](https://opensource.apple.com/source/libpthread/libpthread-301.30.1/pthread/pthread.h.auto.html)

## 3줄 요약

- 스레드 생성 & 실행
  - [pthread_create](#pthread_create)
- 스레드 종료 후 자원 회수
  - 스레드 끝날 때까지 기다린다면: [pthread_join](#pthread_join)
  - 기다리지 않는다면: [pthread_detach](#pthread_detach)

스레드 생성과 자원 회수는 malloc과 free처럼 짝을 이루는 관계

## 스레드 만들고 실행하기

### pthread_create

```yaml
pthread: 스레드 id, fd와 비슷하나 구현에 따라 정수형이 아니라 구조체일 수 있음
attr: 스레드 세부 속성
  NULL: 기본값
start_routine: 실행할 함수
arg: `start_routine`에 들어갈 인수
```

- 새로운 자식 스레드를 생성하고 실행
- 자식 스레드가 끝나기까지 기다리지 **않음**
- 생성된 스레드는 **종료되어도 자원(메모리) 반납을 하지 않음**

### 예시

```c
// 공통 코드
#include <stdio.h>
#include <pthread.h>
#include <stdbool.h>

typedef void *(*routine)(void *);

typedef struct s_data {
	int a;
} data;

void *thread_func(void *arg)
{
	const data *val = arg;

	printf("[스레드] 인자 %d로 실행된 함수\n",val->a);
	return NULL;
}
```

#### 그냥 실행했을 시

```c
int main(void) {
	pthread_t thread;

	pthread_create(&thread, NULL, thread_func, &((data){123}));
	return 0;
}
/* 출력 없이 종료 */
```

#### main문에서 무한루프로 기다릴 시

```c
int main(void) {
	pthread_t thread;

	pthread_create(&thread, NULL, thread_func, &((data){123}));
	printf("[main] 기다리는 중\n");
	while (true) {};
	return 0;
}
/*
[main] 기다리는 중
[스레드] 인자 123로 실행된 함수
*/
```

## 스레드 종료 후 자원 회수하기

### pthread_join / pthread_detach를 쓰는 이유는?

#### 사용 안할 시

```yaml
❯ valgrind --leak-check=full --show-leak-kinds=all ./learn_pthread

HEAP SUMMARY:
    in use at exit: 272 bytes in 1 blocks
  total heap usage: 2 allocs, 1 frees, 4,368 bytes allocated

272 bytes in 1 blocks are possibly lost in loss record 1 of 1
  by 0x49075D9: pthread_create@@GLIBC_2.34 (pthread_create.c:623)
  by 0x1091F9: init_pthread (in /home/scarf/Repo/learn_pthread/learn_pthread)

LEAK SUMMARY:
  possibly lost: 272 bytes in 1 blocks
ERROR SUMMARY:
  1 errors from 1 contexts (suppressed: 0 from 0)
```

메모리 누수 발생

#### 사용 시

```yaml
HEAP SUMMARY:
    in use at exit: 0 bytes in 0 blocks
  total heap usage: 2 allocs, 2 frees, 4,368 bytes allocated
All heap blocks were freed -- no leaks are possible
ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```

스레드 종료 후 자원이 반환(free)됨

### pthread_join

```yaml
pthread: 합칠 스레드
retval: 받아올 반환값
```

- 인자로 준 스레드가 종료할 때까지 대기
- 종료된 스레드의 자원 회수

### pthread_detach

```yaml
pthread: detach할 스레드
```

- 인자로 준 스레드를 **detach**상태로 만듬
- **detached**된 스레드는
  - 종료 시 자동으로 자원이 반환됨
  - 다시 join이 불가능

## 순서도

```c
메인 스레드
    |
    V
main(int argc, char *argv[])
    |
    V
// 스레드 생성 및 실행
pthread_create(pthread, attr, start_routine, arg)
    |               |
    V               V
이후 코드 실행...  자식 스레드
    |           (pthread, attr, start_routine, arg)
    |               |
    |               V
    |           start_routine(arg) 실행...
    |               |
    |               V
    |              종료
    |               /
    V              V
// 스레드가 끝날 때까지 대기
pthread_join(pthread)
    |
    V
return(0);
```