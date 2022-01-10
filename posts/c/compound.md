---
title: compound literal로 일회용 배열/구조체 만들기
---

## compound literal이란

- `(자료형){생성자 목록}` 형식으로 선언하는 익명 객체
- 일회용 **배열**, **구조체** 등이 필요할 때 사용
- [cpp레퍼런스](https://en.cppreference.com/w/c/language/compound_literal)

## 활용

### 배열

```c
#include <stdio.h>

void passArr(int arr[]) {
	for (int i = 0; i < 3; i++)
		printf("%d ", arr[i]);
	printf("\n");
}

int main(void){
  	int arr[] = {1, 2, 3};
  	passArr(arr);
	passArr((int[]){1, 2, 3});
	return 0;
}

/*
1 2 3
1 2 3
/*
```

### 구조체

```c
#include <stdio.h>

typedef struct s_vec2 {
	int x;
	int y;
} vec2;

void passVal(vec2 vec) {
	printf("%d %d\n", vec.x, vec.y);
}

void passRef(vec2 *vec) {
	printf("%d %d\n", vec->x, vec->y);
}

int main(void){
	vec2 vec_a = {1, 2};
	passVal(vec_a);
	passVal((vec2){1, 2});
	vec2 vec_b = {.x=3, .y=4};
	passRef(&vec_b);
	passRef(&(vec2){.x=3, .y=4});
	return 0;
}
/*
1 2
1 2
3 4
3 4
*/
```
