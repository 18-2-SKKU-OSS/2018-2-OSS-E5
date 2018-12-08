'''
삼분 탐색 (Ternary Search)
함수의 최대나 최소점을 찾는 알고리즘으로 이진 탐색과 그 동작방법이 비슷합니다. 배열을 세 개의
부분으로 나눠 분할 정복 방법으로 탐색을 진행하게 됩니다.
'''
from __future__ import print_function

import sys

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

# precision 값보다 작아지면 선형 탐색을 시작합니다.
precision = 10

# 탐색 배열이 충분이 작아지면 선형탐색을 실시하게 됩니다.
def lin_search(left, right, A, target):
    for i in range(left, right+1):
        if(A[i] == target):
            return i

# 반복문을 이용한 삼분탐색
def ite_ternary_search(A, target):
    left = 0
    right = len(A) - 1;
    while(True):
        if(left<right):
            
            if(right-left < precision):
                return lin_search(left,right,A,target)

            oneThird = (left+right)/3+1;
            twoThird = 2*(left+right)/3+1;
            
            if(A[oneThird] == target):
                return oneThird
            elif(A[twoThird] == target):
                return twoThird
            
            elif(target < A[oneThird]):
                right = oneThird-1
            elif(A[twoThird] < target):
                left = twoThird+1
            
            else:
                left = oneThird+1
                right = twoThird-1
        else:
            return None

# 재귀를 이용한 삼분탐색
def rec_ternary_search(left, right, A, target):
    if(left<right):
        
        if(right-left < precision):
            return lin_search(left,right,A,target)

        oneThird = (left+right)/3+1;
        twoThird = 2*(left+right)/3+1;

        if(A[oneThird] == target):
            return oneThird
        elif(A[twoThird] == target):
            return twoThird
        
        elif(target < A[oneThird]):
            return rec_ternary_search(left, oneThird-1, A, target)
        elif(A[twoThird] < target):
            return rec_ternary_search(twoThird+1, right, A, target)
        
        else:
            return rec_ternary_search(oneThird+1, twoThird-1, A, target)
    else:
        return None

#입력값이 정렬이 됬는지 확인 해주는 함수
def __assert_sorted(collection):
    if collection != sorted(collection):
        raise ValueError('Collection must be sorted')
    return True


if __name__ == '__main__':
    user_input = raw_input('Enter numbers separated by coma:\n').strip()
    collection = [int(item) for item in user_input.split(',')]

    try:
        __assert_sorted(collection)
    except ValueError:
        sys.exit('Sequence must be sorted to apply the ternary search')

    target_input = raw_input('Enter a single number to be found in the list:\n')
    target = int(target_input)
    result1 = ite_ternary_search(collection, target)
    result2 = rec_ternary_search(0, len(collection)-1, collection, target)
    
    if result2 is not None:
        print('Iterative search: {} found at positions: {}'.format(target, result1))
        print('Recursive search: {} found at positions: {}'.format(target, result2))
    else:
        print('Not found')
