"""
점프 탐색 (Jump Search) 
이진 탐색과 마찬가지로 정렬된 배열을 대상으로 하는 탐색 알고리즘이다. 타겟 값보다 큰 값이 나올 때까지 
순차적으로 배열요소에 접근을 하게 된다. 그리고
"""
from __future__ import print_function

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3
    
import math
def jump_search(arr, x):
    n = len(arr)
    step = int(math.floor(math.sqrt(n)))
    prev = 0
    while arr[min(step, n)-1] < x:
        prev = step
        step += int(math.floor(math.sqrt(n)))
        if prev >= n:
            return -1

    while arr[prev] < x:
        prev = prev + 1
        if prev == min(step, n):
            return -1
    if arr[prev] == x:
        return prev
    return -1


#입력값이 정렬이 됬는지 확인 해주는 함수
def __assert_sorted(collection):
    if collection != sorted(collection):
        print('error: Collection must be sorted')
        raise ValueError('Collection must be sorted')
    return True

if __name__ == '__main__':
    import sys
    user_input = raw_input('Enter numbers separated by comma:\n').strip()
    collection = [int(item) for item in user_input.split(',')]
    try:
        __assert_sorted(collection)
    except ValueError:
        sys.exit('Sequence must be sorted to apply binary search')

    target_input = raw_input('Enter a single number to be found in the list:\n')
    target = int(target_input)
    
    #binary_search 함수 사용
    result = jump_search(collection, target)
    if result is not None:
        print('{} jump search found at positions: {}'.format(target, result))
    else:
        print('Not found')
