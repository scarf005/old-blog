---
title: var vs let vs const
---

## 3줄 요약

- 무조건 `const`로 선언
- 값이 변해야 할 일이 있으면 `let`으로 선언
- `var`은 쓰지 말자

## var

- `ES6` / `ECMAScript 2015` 이전까지 **유일한** 변수 정의 방식
- [호이스팅](#호이스팅)으로 인해 의도치 않은 결과가 발생함

## let

- `ES6` / `ECMAScript 2015` **이후**로 추가된 **변수** 정의 방식
- 블록 안에서만 사용 가능

```js
let x = 1
{
  let x = 2
  console.log(x)
  // 예상값: 2
}

console.log(x)
// 예상값: 1

> 2
> 1
```

```js
let x = 1
{
  console.log(x)
  let x = 2
}
> Uncaught ReferenceError: Cannot access 'x' before initialization
    at <anonymous>:4:15
```

- [let에서도 호이스팅이 일어난다](#Temporal-Dead-Zone-(TDZ))

## const
- `ES6` / `ECMAScript 2015` **이후**로 추가된 **상수** 정의 방식
- 블록 안에서만 사용 가능

## 호이스팅
- [mdn 레퍼런스](https://developer.mozilla.org/ko/docs/Glossary/Hoisting)
- **초기화**가 아닌 **선언**은 모두 호이스팅 대상
  - 예외: `var`

### Temporal Dead Zone (TDZ)

- `let`과 `var`도 **호이스팅 대상**
- 하지만 값이 `var`과 달리 `undefined`로 초기화되지 않으므로 `TDZ` 상태에 놓이게 됨
- 아직 값이 초기화되지 않으므로 참조시 [ReferenceError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError) 발생
- [mdn 레퍼런스](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz)

### var
```js
var_선언
var var_선언
<- undefined

var_초기화
var var_초기화 = 1
<- undefined
```

### 익명 global (키워드 없이 선언)

```js
global_초기화
global_초기화 = 2
<- Uncaught ReferenceError: global_초기화 is not defined
    at <anonymous>:1:1
```

### let, const

```js
let_선언
let let_선언
<- Uncaught ReferenceError: let_선언 is not defined
    at <anonymous>:1:1

let_초기화
let let_초기화 = 3
<- Uncaught ReferenceError: let_초기화 is not defined
    at <anonymous>:1:1

const_초기화
const const_초기화 = 4
<- Uncaught ReferenceError: const_초기화 is not defined
    at <anonymous>:1:1
```

