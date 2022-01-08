---
title: 자바스크립트 화살표 함수 => 쓰기
date: 2022-01-08
---

## 화살표 함수가 모지

```js
function myFunc(a, b) { return a + b }
const myArrowFunc = (a, b) => a + b

const a = 3, b = 4
console.log(myFunc(a, b))
console.log(myArrowFunc(a, b))

<- 7
<- 7
```

## 어떻게 쓰지

[mdn 한글 레퍼런스](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/Arrow_functions)


### 인자 0개

[고급 사용법](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions#advanced_syntax)
```js
const noArg = () => 3

noArg()
<- 3

const oneLine = () => console.log("한 줄이면 괄호 필요 없음")

oneLine()
<- 한 줄이면 괄호 필요 없음
```

### 인자 1개
```js
const oneArg = num => num * 4

oneArg(10)
<- 40
```

### 인자 n개

```js
const manyArg = (a, b) => a + b

manyArg(3, 4)
<- 7
```

### 여러 줄 함수
```js
const manyLine = (a, b) => {
  console.log(`첫째 인수는 ${a}`)
  console.log(`둘째 인수는 ${b}`)
  return `이거는 반환값`
}

manyLine(3, 4)
<- 첫째 인수는 3
<- 둘째 인수는 4
<- '이거는 반환값'
```

## 화살표 함수와 this

[화살표 함수를 메소드로 쓸 수 있을까?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions#arrow_functions_used_as_methods)

- 자기만의 `this` 가 없다
- 자기 바로 바깥 구문의 `this`를 가진다



## 언제 쓸까

### [메소드 체이닝](/posts/javascript/method_chain)할때 보기 예쁘다

```js
const arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr
  .filter(e => e % 2 === 0)
  .map(e => e ** 2)
<- (5) [0, 4, 16, 36, 64]
```

```js
const arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr
  .filter(function(e) {return e % 2 === 0 })
  .map(function(e) { return e ** 2 })
<-(5) [0, 4, 16, 36, 64]
```

- 쓸 수 있는 경우에 많이 쓰자

### 비동기 함수를 써야 할때

[참고](https://developer.mozilla.org/ko/docs/Web/API/setTimeout#this_%EB%AC%B8%EC%A0%9C)

```js
class Person {
  constructor(name) {
    this.name = name
  }

  hi() {
    console.log(`hi, i'm ${this.name}`)
  }

  hiDelayed() {
    setTimeout(function() {
      console.log(`hi, i'm ${this.name}`), 1000
    })
  }

  hiDelayedTradFix() {
    const that = this
    setTimeout(function() {
      console.log(`hi, i'm ${that.name}`), 1000
    })
  }

  hiDelayedArrow() {
    setTimeout(() => {
      console.log(`hi, i'm ${this.name}`), 1000
    })
  }
}

mary = new Person('mary')
mary.hi()
<- hi, i'm mary
mary.hiDelayed()
<- hi, i'm
mary.hiDelayedTradFix()
<- hi, i'm mary
mary.hiDelayedArrow()
<- hi, i'm mary
```

## 언제 쓰지 말까

- 좀 복잡하다
- [관련 정리글](https://vmarchesin.medium.com/javascript-arrow-functions-and-closures-4e53aa30b774)
- TODO
<!--

- `constructor`
- `yield`
-
```js
const obj = {
    i: 10,
    a: () => console.log(this.i, this),
    b: function() { console.log(this.i, this) }
}

obj.a()
<- undefined
<- Window {0: global, window: Window, self: Window, document: document, name: '', location: Location, …}

obj.b()
<- 10
<- {i: 10, a: ƒ, b: ƒ}
```
-->