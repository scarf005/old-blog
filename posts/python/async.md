---
title: asyncio로 파이썬에서 비동기 프로그래밍 하기
---

[acyncio](https://docs.python.org/ko/3/library/asyncio.html)

## 코루틴이 뭐지?

- 서브루틴(subroutine)/프로시저(procedure): 명령어 묶음.
- 함수: 값을 반환하는 서브루틴
- 코루틴: 일시정지 할 수 있는 함수

## asyncio 써보기

비동기를 쓰려면 `async` 랑 `await` 구문을 쓸 줄 알아야 한다.

- async: 비동기 함수를 정의한다
- await: 결과값을 받을 때까지 행동을 멈춘다

```py
import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())
# hello
# (1초)
# world
```