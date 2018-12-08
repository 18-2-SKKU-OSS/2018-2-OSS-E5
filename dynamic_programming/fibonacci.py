"""
이것은 피보나치 시퀀스 문제에 대한 다이나믹 프로그래밍 솔루션의 순수한 파이썬 구현입니다.
코드를 보면 알 수 있듯이, 동적계획법 (DP)을 사용하여 구현한 이 알고리즘은
재귀로 구현한 알고리즘에 비해 bottom-up 방식으로 값을 채워나간다는 점에서 차이가 있으며
실제로 같은 값을 여러번 계산하지 않아도 되기 때문에 불필요한 반복계산을 줄이는 효과가 있습니다.
순환식을 계산할때 사용이 되며 DP을 이용하면 오버헤드를 수반하지 않는 장점이 있습니다.
"""
from __future__ import print_function


class Fibonacci:

    def __init__(self, N=None):
        self.fib_array = []
        if N:
            N = int(N)
            self.fib_array.append(0)
            self.fib_array.append(1)
            for i in range(2, N + 1):
                self.fib_array.append(self.fib_array[i - 1] + self.fib_array[i - 2])
        elif N == 0:
            self.fib_array.append(0)

    def get(self, sequence_no=None):
        if sequence_no != None:
            if sequence_no < len(self.fib_array):
                return print(self.fib_array[:sequence_no + 1])
            else:
                print("Out of bound.")
        else:
            print("Please specify a value")


if __name__ == '__main__':
    print("\n********* Fibonacci Series Using Dynamic Programming ************\n")
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    print("\n Enter the upper limit for the fibonacci sequence: ", end="")
    try:
        N = eval(raw_input().strip())
        fib = Fibonacci(N)
        print(
            "\n********* Enter different values to get the corresponding fibonacci sequence, enter any negative number to exit. ************\n")
        while True:
            print("Enter value: ", end=" ")
            try:
                i = eval(raw_input().strip())
                if i < 0:
                    print("\n********* Good Bye!! ************\n")
                    break
                fib.get(i)
            except NameError:
                print("\nInvalid input, please try again.")
    except NameError:
        print("\n********* Invalid input, good bye!! ************\n")
