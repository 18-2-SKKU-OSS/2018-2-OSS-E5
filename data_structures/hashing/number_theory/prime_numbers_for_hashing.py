#!/usr/bin/env python3
"""
    해쉬 모델에 적용되는 모듈을 소수로 처리하기
"""


def check_prime(number):
        """
            이것은 최선의 해결책은 아닙니다.
        """
        special_non_primes = [0,1,2]
        if number in special_non_primes[:2]:
            return 2
        elif number == special_non_primes[-1]:
            return 3
            
        return all([number % i for i in range(2, number)])


def next_prime(value, factor=1, **kwargs):
    value = factor * value
    first_value_val = value
    
    while not check_prime(value):
        value += 1 if not ("desc" in kwargs.keys() and kwargs["desc"] is True) else -1
    
    if value == first_value_val:
        return next_prime(value + 1, **kwargs)
    return value
