---
title: 세미콜론(;) 없는 언어가 좋아
date: 2022-01-23 21:31:31 +09:00
---

## `;`가 몰까

- 우리말로는 쌍반점
- 영어권에써 쓰지만 우리는 쓰지 않음

### 주로 쓰는 경우
- 원인 + 결과
`She didn't sleep all night; the build failed.` (; == because)
`The build failed; she didn't sleep all night` (; == so)
- 조건 + 결과
`Send the package; I'll pay.` (; == then)
- 나열하는데 나열 대상에 쉼표가 들어가면

## 프로그래밍에서 쓰이게 된 계기
[세미콜론의 역사](https://betterprogramming.pub/a-brief-history-of-the-8efda9dde2b8)
[quora 답변](https://stackoverflow.com/questions/4701137/why-do-some-languages-need-semicolons)

- 과거 프로그래밍은 한 줄로 길게 입력해야 해서 구별자가 필요했다
- 그 중에서 잘 안 쓰이는 문장부호인 `;`가 초기 언어(Algol, C...)들에서 주로 쓰였다
- 초기 언어의 문법과 유사한 새 언어들이 나오면서 관습으로 내려왔다

## 어디에서 주로 쓰일까

### 선언 구별자
`a = 3`, `b = 0`를 한 줄에 합치면 `a = 3b = 0`인지 확인하기 어렵다. 이럴 때 구별자가 필요하다.

### 선언 종결자
컴파일러가 구문을 분석할 때 어디까지 선언이 이어지는지 확인해야 한다.

## 쓰지 않는 언어들은?

### 키워드별로 선언의 길이가 정해진 언어

- 어셈블리
```asm
; hello-DOS.asm - single-segment, 16-bit "hello world" program
;
; assemble with "nasm -f bin -o hi.com hello-DOS.asm"

    org  0x100        ; .com files always start 256 bytes into the segment

    ; int 21h is going to want...

    mov  dx, msg      ; the address of or message in dx
    mov  ah, 9        ; ah=9 - "print string" sub-function
    int  0x21         ; call dos services

    mov  ah, 0x4c     ; "terminate program" sub-function
    int  0x21         ; call dos services

    msg  db 'Hello, World!', 0x0d, 0x0a, '$'   ; $-terminated message
```
[코드 출처](https://montcs.bloomu.edu/Information/LowLevel/Assembly/hello-asm.html)

- 베이직
```basic

```

- 리스프
```lisp
(defun hello ()
  (format t "Hello, World!~%"))
```

### 줄바꿈 (`\n`)을 선언 종결자로 쓰는 언어
```python

def sayhello(name: str) -> str:
    if name != "애옹":
        return f"안녕, {name}"
    else:
        return "으에엑"
```

```go
package main

import "fmt"

func main() {
	fmt.Println("안녕, 세상")
}
```

```kotlin
fun main() {
    println("안녕, 세상")
}
```

## 세미콜론 없는 언어를 좋아하는 이유
물론 주관적인 기준이라 근거가 될 수 없지만...

### 세미콜론을 치지 않아도 되서
- 처음 배운 언어가 액션스크립트랑 파이썬
- 액션스크립트는 세미콜론 빼먹어서 생기는 오류가 너무 많아서 힘들었음

### 보기 더 예뻐서?
- 아무래도 처음 배운 언어가 파이썬이라서...

### 메소드 체이닝 할 때 편하다
```js
foo
  .map(x => x ** 2)
  .filter(x => x > 6)
  (...)
  .map(x => x + 16)
  .find(x => x == 4);
```
- 만약 마지막 메소드를 맨 처음으로 옮겨야 한다면?
- 메소드를 새로 추가해야 한다면?
- 메소드 목록 중간에 세미콜론을 지우지 않아 거기까지만 실행되었다면?

사소하지만 세미콜론을 지우고 새로 추가하는 게 의외로 손이 많이 간다

## 결론
물론 취향 차이지만 아무래도 세미콜론 없는 언어에 좀 더 관심이 생기는 거는 어쩔 수 업다

줄바꿈 조.아