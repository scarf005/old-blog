---
title: 자바스크립트 method chaining 써보기
date: 2022-01-08
---


## 무작위 배열 만들기

```js
const randint = (min, max) => Math.floor(Math.random() * (max - min)) + min
const arr = Array.from({length: 20}, () => randint(1, 20))

> arr
(20) [4, 3, 15, 14, 16, 15, 4, 18, 18, 4, 16, 17, 1, 3, 11, 19, 9, 15, 12, 12]
```