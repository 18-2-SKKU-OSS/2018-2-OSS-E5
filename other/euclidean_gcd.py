"""
유클리드 호제법은 2개의 자연수 또는 정식의 최대공약수를 구하는 알고리즘의 하나이다. 
호제법이란 말은 두 수가 서로 상대방 수를 나누어서 결국 원하는 수를 얻는 알고리즘을 나타낸다. 
2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 
이 성질에 따라, b를 r로 나눈 나머지 r'를 구하고, 
다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다.
"""
from __future__ import print_function
# https://en.wikipedia.org/wiki/Euclidean_algorithm

def euclidean_gcd(a, b):
    while b:
        t = b
        b = a % b
        a = t
    return a

def main():
    print("GCD(3, 5) = " + str(euclidean_gcd(3, 5)))
    print("GCD(5, 3) = " + str(euclidean_gcd(5, 3)))
    print("GCD(1, 3) = " + str(euclidean_gcd(1, 3)))
    print("GCD(3, 6) = " + str(euclidean_gcd(3, 6)))
    print("GCD(6, 3) = " + str(euclidean_gcd(6, 3)))

if __name__ == '__main__':
    main()
