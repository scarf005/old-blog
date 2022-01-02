---
title: comprehension 표현식 써보기
date: 2022-01-02
---


파이썬을 만든 귀도 반 로섬은 [2005년 글](https://www.artima.com/weblogs/viewpost.jsp?thread=98196)에서 `map`, `filter` `reduce` 같은 함수형 프로그래밍보다 `list comprehension` 이 더 읽기에 좋다고 했다. 그렇다면 이거는 어떻게 쓰는 걸까?

## comprehension이란?

리스트를 간결하게 만들어낼 수 있는 문법이다. 기존에 `[0, 1, 2, 3, 4, 5]`을 만들려고

```python
lst = []
for i in range(6):
  lst.append(i)
```

이런 식을 썼었다면

```python
lst = [i for i in range(6)]
```
`list comprehension`으로는 이렇게 한 줄로 가능하다.

```python
[x for x in range(6) if x % 2 == 0]
# [0, 2, 4]
```

```py
[x if x % 2 == 0 else '!' for x in range(6)]
# [0, '!', 2, '!', 4, '!']
```

또 내부에서 간단하게 `if-else`문을 쓸 수 있다.

```py
[수식 for 원소 in 리스트 if 조건문]
```
문법이 조금 다르지만 기본 구조는 위와 같다.

```py
[[0 for _ in range(3)] for _ in range(2)]
# [[0, 0, 0],
# [0, 0, 0]]
```
중첩해서 쓸 수도 있다.