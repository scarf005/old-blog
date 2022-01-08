---
title: 자바스크립트 method chaining 써보기
---


## 시작하기 전에

### [화살표 함수 쓰기](/posts/javascript/arrow)

```js
const isEven = n => n % 2 === 0

isEven(20)
<- true
```

### 무작위 숫자 생성

```js
const randint = (min, max) => Math.floor(Math.random() * (max - min)) + min
```

### 배열 생성
```js
const arr = Array.from({length: 20}, () => randint(1, 20))

arr
<- (20) [4, 3, 15, 14, 16, 15, 4, 18, 18, 4, 16, 17, 1, 3, 11, 19, 9, 15, 12, 12]
```

## 기초 응용

```js