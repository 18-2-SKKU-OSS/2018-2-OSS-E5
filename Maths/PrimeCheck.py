#소수인지 판별하는 함수

import math

def primeCheck(number):
    if number % 2 == 0 and number > 2: 
        return False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2))

def main():
    print(primeCheck(37)) #참
    print(primeCheck(100)) #거짓
    print(primeCheck(77)) #거짓

if __name__ == '__main__':
	main()
