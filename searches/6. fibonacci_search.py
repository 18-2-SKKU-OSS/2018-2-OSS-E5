"""
피보나치 탐색 (fibonacci search)
이진 탐색과 비슷하여 이미 정렬된 데이터의 집합들로 부터 특정한 키를 찾는 알고리즘이다. 특별하게
피보나치 탐색은 피보나치 수열을 이용하여 탐색 구간을 정하게 된다.
"""
from __future__ import print_function

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

#피보나치 탐색
def fibonacci_search(arr, x, n):
    """
    input값은 반드시 정렬 된 채로 주어져야 합니다.
    그러지 않으면 원하지 않는 결과값이 나올 수 있습니다.
    :param arr : 탐색을 진행할 배열
    :param x : 탐색을 진행할 키(key) 값
    :param n : 배열의 크기
    ;return : 키 값이 있는 위치(index), 없을 경우 None
    """
    fibMMm2 = 0  # (m-2)'th Fibonacci No. 
    fibMMm1 = 1   # (m-1)'th Fibonacci No. 
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci

    while (fibM < n): 
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM  = fibMMm2 + fibMMm1
  
    offset = -1
  
 
    while (fibM > 1):
        i = min(offset+fibMMm2, n-1)
  
        if (arr[i] < x):
            fibM  = fibMMm1
            fibMMm1 = fibMMm2 
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif (arr[i] > x):
            fibM  = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i
  

    if(fibMMm1 and arr[offset+1]==x):
        return offset+1
  
    return None

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
    
    n = len(collection)
    print("Found at index:", 
            fibonacci_search(collection, target, n))

