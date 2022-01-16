---
title: 함수 포인터를 써보자
date: 2022-01-14 16:42:19 +09:00
---

## 함수 포인터란

### 선언

- `반환값 (*이름)(인자 목록)`
- 포인터가 값의 주소를 담듯 함수의 주소를 담음

```c
#include <stdio.h>

void sayhello(void) {
  printf("Hello World\n");
}

int main(void) {
  int value = 3;
  int *ptr = &value;
  printf("포인터가 가리키는 값은 %d\n", *ptr);

  void (*fp1)() = &sayhello;
  (*fp1)();
  int (*fp2)(int) = &saynum;
  (*fp2)(10);
  return 0;
}
포인터가 가리키는 값은 3
Hello World
입력값: 10
```

일반 포인터를 쓰는 것과 비슷하게

- 참조할 함수의 주소를 대입하고
- 별(\*) 기호로 역참조해 쓴다.

### 간략하게 사용

```c
int main(void) {
  void (*fp3)() = sayhello;
  fp3();
  int (*fp4)(int) = saynum;
  fp4(10);
  return 0;
}
Hello World
입력값: 10
```

그런데 함수의 이름은 고유하니

- & 기호를 넣을 필요없이 이름만 쓰고

괄호를 이용해 함수와 같이 쓰는 건 똑같으므로

- 역참조와 괄호도 생략해도 된다.

```c
typedef void (*myfunc)(int);

void example(myfunc f, int num) {
  f(num);
}

int main(void) {
  myfunc func = saynum;
  func(5);
  example(saynum, 123);
  return 0;
}
입력값: 5
입력값: 123
```

typedef를 이용해 자료형을 지정하면 쓰기 더 편하다.

## 함수 포인터 써보기

### 조건문을 쓰는 방식(기존)

```c

#include <stdio.h>

int calc(int which, int a, int b) {
  int res;
  switch (which) {
    case 0:
      res = a + b;
      break;
    case 1:
      res = a - b;
      break;
    case 2:
      res = a * b;
      break;
    case 3:
      res = a / b;
      break;
    default:
      return 0;
  }
  return res;
}

int main(void) {
  int a = 12, b = 5;

  printf("a: %d, b: %d\n", a, b);
  printf("덧셈 결과: %d\n", calc(0, a, b));
  printf("뺄셈 결과: %d\n", calc(1, a, b));
  printf("곱셈 결과: %d\n", calc(2, a, b));
  printf("나눗셈 결과: %d\n", calc(3, a, b));
  return 0;
}
a: 12, b: 5
덧셈 결과: 17
뺄셈 결과: 7
곱셈 결과: 60
나눗셈 결과: 2
```

- `#define`
- `enum`

을 쓴다면 좀 더 읽기 편하겠지만 거듭제곱, 나머지... 10가지 기능을 더 추가해야 한다면? `switch`문이 계속 길어지게 된다.

### 함수 포인터를 이용한 방식

```c
typedef int (*calcfunc)(int a, int b);

int add(int a, int b) {
  return a + b;
}
int sub(int a, int b) {
  return a - b;
}
int mul(int a, int b) {
  return a * b;
}
int div(int a, int b) {
  return a / b;
}

int calc(calcfunc func, int a, int b) {
  return func(a, b);
}

int main(void) {
  int a = 12, b = 5;
  printf("a: %d, b: %d\n", a, b);

  char* which[] = {"덧셈", "뺄셈", "곱셈", "나눗셈"};
  calcfunc func[] = {add, sub, mul, div};
  for (int i = 0; i < 4; i++) {
    printf("%s 결과: %d\n", which[i], calc(func[i], a, b));
  }
  return 0;
}
a: 12, b: 5
덧셈 결과: 17
뺄셈 결과: 7
곱셈 결과: 60
나눗셈 결과: 2
```

이제 `calc` 함수를 변경할 필요 없이 다양한 함수를 입력값으로 넣어 유연하게 사용할 수 있다.