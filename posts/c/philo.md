---
title: 냉혹한 philosopher의 세계
---

## 식사하는 철학자 문제

- [위키피디아](https://en.wikipedia.org/wiki/Dining_philosophers_problem)
- [결과 확인](https://nafuka11.github.io/philosophers-visualizer/)

목표: **스레드**, **뮤텍스**/**세마포어**로 식사하는 철학자 문제 해결

## 허용 함수 목록

### 기본 기능
- <string.h>
  - memset
- <stdio.h>
  - printf
- <stdlib.h>
  - malloc
  - free
- <unistd.h>
  - write
  - usleep
- <sys/time.h>
  - gettimeofday

### 멀티스레딩
- <pthread.h>
  - pthread_create
  - pthread_detach
  - pthread_join
  - pthread_mutex_init
  - pthread_mutex_destroy
  - pthread_mutex_lock
  - pthread_mutex_unlock

## 목차

- [pthread가 뭔지 몰?루](thread.md)
- [mutex가 뭔지 몰?루](mutex.md)

## 보너스 허용 함수 목록

### 기본 기능

- <string.h>
  - memset
- <stdio.h>
  - printf
- <stdlib.h>
  - malloc
  - free
  - exit
- <unistd.h>
  - write
  - usleep
- <sys/time.h>
  - gettimeofday

### 멀티프로세싱

- <unistd.h>
  - fork
  - kill
- <sys/wait.h>
  - waitpid

### 멀티스레딩

- <pthread.h>
  - pthread_create
  - pthread_detach
  - pthread_join

- <semaphore.h>
  - sem_open
  - sem_close
  - sem_post
  - sem_wait
  - sem_unlink
