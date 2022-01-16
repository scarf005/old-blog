---
title: mutex가 몬지 몰?루
date: 2022-01-15 12:53:43 +09:00
---

## 3줄 요약

- 뮤텍스(mutex)는 공중전화 부스 **열쇠**와 같다
- 열쇠를 가진 사람만 전화(작업)를 할 수 있다(pthread_mutex_lock)
- 전화를 하고 나면 다른 사람이 쓸 수 있게 열쇠를 반납한다(pthread_mutex_unlock)

## mutex가 필요한 상황

```c
#include <stdio.h>
#include <pthread.h>
#include <stdbool.h>

typedef struct s_data {
	int id;
	int *val;
	pthread_mutex_t *mutex;
} data;

void *thread_func(void *arg) {
	data *a = (data *)arg;
	for (int i = 0; i < 100000; i++)
		*a->val += 1;

	printf("[스레드 %d] val의 값을 100000만큼 증가시켰다. val:%d\n", a->id, *a->val);
}

int main(void) {
	const int size = 1;

	// 변화시킬 값
	int num = 0;
	int *val = &num;

	// 스레드 생성
	data arg[size];
	pthread_t thread[size];
	pthread_mutex_t mutex;

	pthread_mutex_init(&mutex, NULL);
	for (int i = 0; i < size; i++) {
		arg[i].id = i;
		arg[i].mutex = &mutex;
		arg[i].val = val;
		printf("%d번째 스레드 생성\n", i);
		pthread_create(&(thread[i]), NULL, thread_func, &arg[i]);
	}
	for (int i = 0; i < size; i++)
		pthread_join(thread[i], NULL);
	return 0;
}

0번째 스레드 생성
[스레드 0] val의 값을 100000만큼 증가시켰다. val:100000
```

별 문제 없어보인다. 그런데 val의 값을 여러 스레드가 동시에 접근한다면?

```c
...
const int size = 2;
...

0번째 스레드 생성
1번째 스레드 생성
2번째 스레드 생성
[스레드 1] val의 값을 100000만큼 증가시켰다. val:100068
[스레드 2] val의 값을 100000만큼 증가시켰다. val:100215
[스레드 0] val의 값을 100000만큼 증가시켰다. val:200215
```

서로 동시에 값을 조작하니 원하는 결과가 나오지 않는다.
스레드가 열쇠(mutex)를 가질 때까지 기다렸다가 열쇠를 갖고 있어야만 작업을 할 수 있게 한다면?

```c
void *thread_func(void *arg) {
	data *a = (data *)arg;

	pthread_mutex_lock(a->mutex);
	printf("[스레드 %d] 뮤텍스를 획득했다.\n", a->id);
	for (int i = 0; i < 100000; i++)
		*a->val += 1;
	printf("[스레드 %d] val의 값을 100000만큼 증가시켰다. val:%d\n", a->id, *a->val);
	pthread_mutex_unlock(a->mutex);
	printf("[스레드 %d] 뮤텍스를 반납했다.\n", a->id);
}
0번째 스레드 생성
1번째 스레드 생성
[스레드 0] 뮤텍스를 획득했다.
2번째 스레드 생성
[스레드 0] val의 값을 100000만큼 증가시켰다. val:100000
[스레드 0] 뮤텍스를 반납했다.
[스레드 1] 뮤텍스를 획득했다.
[스레드 1] val의 값을 100000만큼 증가시켰다. val:200000
[스레드 1] 뮤텍스를 반납했다.
[스레드 2] 뮤텍스를 획득했다.
[스레드 2] val의 값을 100000만큼 증가시켰다. val:300000
[스레드 2] 뮤텍스를 반납했다.
```

## 참고자료

[pthread_mutex_init](https://linux.die.net/man/3/pthread_mutex_init)
[pthread_mutex_destroy](https://linux.die.net/man/3/pthread_mutex_destroy)
[pthread_mutex_lock](https://linux.die.net/man/3/pthread_mutex_lock)