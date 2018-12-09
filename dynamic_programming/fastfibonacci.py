#!/usr/bin/python
# encoding=utf8

"""
이 프로그램은 O (log (n))에서 n 번째 피보나치 수를 계산합니다.
1 초 이내에 F (1000000)를 계산할 수 있습니다.
이 알고리즘은이 무고한 정체성 (수학적 유도로 입증 될 수 있음)을 기반으로합니다.
이러한 ID는 행렬 지수 알고리즘에서 추출 할 수 있습니다. 어떤 의미에서 이 알고리즘은 
중복 계산이 제거 된 행렬 지수 알고리즘입니다. 그것은 매트릭스 지수보다 
더 빠른 상수 인자가되어야하지만, 점근 적 시간 복잡성은 여전히 동일합니다.
"""
from __future__ import print_function
import sys


# returns F(n)
def fibonacci(n: int):  # noqa: E999 This syntax is Python 3 only
    if n < 0:
        raise ValueError("Negative arguments are not supported")
    return _fib(n)[0]


# returns (F(n), F(n-1))
def _fib(n: int):  # noqa: E999 This syntax is Python 3 only
    if n == 0:
        # (F(0), F(1))
        return (0, 1)
    else:
        # F(2n) = F(n)[2F(n+1) − F(n)]
        # F(2n+1) = F(n+1)^2+F(n)^2
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print("Too few or too much parameters given.")
        exit(1)
    try:
        n = int(args[0])
    except ValueError:
        print("Could not convert data to an integer.")
        exit(1)
    print("F(%d) = %d" % (n, fibonacci(n)))
