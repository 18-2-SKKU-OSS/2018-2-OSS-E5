"""
지수 탐색 (exponential search)
지수 탐색은 두 가지 단계로 나뉜다. 첫째, 타겟 값이 있는 배열 범위를 찾는다. 둘째, 앞에서 찾은 
범위를 바탕으로 이진 탐색을 진행한다. 첫 번째 단계에서 범위를 찾는 방법은, 배열의 크기를 1, 2, 4...
와 같이 지수 함수로 늘려 가면서 찾는다.
"""
from __future__ import print_function
import bisect

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

#지수탐색
def exponential_search(arr, n, x):
    """
    input값은 반드시 정렬 된 채로 주어져야 합니다.
    그러지 않으면 원하지 않는 결과값이 나올 수 있습니다.
    :param arr : 탐색을 진행할 배열
    :param n : 배열의 크기
    :param x : 탐색을 진행할 키(key) 값
    ;return : 키 값이 있는 위치(index), 없을 경우 None
    """
    if (arr[0] == x): 
        return 0
  
    i = 1
    while (i < n and arr[i] <= x):
        i = i*2
  
    return binarySearch(arr, i//2, min(i, n), x)

#이진탐색
def binarySearch(arr, l, r, x):
    """
    :param arr : 탐색을 진행할 배열
    :param l : 탐색 범위의 시작
    :param r : 탐색 범위의 끝 
    :param x : 탐색을 진행할 키(key) 값
    ;return : 키 값이 있는 위치(index), 없을 경우 None
    """
    if (r >= l) :
        mid = l + (r - l) // 2
    
        if (arr[mid] == x): 
            return mid
  
        if (arr[mid] > x) :
            return binarySearch(arr, l, mid-1, x)

        return binarySearch(arr, mid+1, r, x)
  
    return None

if __name__ == '__main__':
    import sys
    user_input = raw_input('Enter numbers separated by comma:\n').strip()
    collection = [int(item) for item in user_input.split(',')]
    
    target_input = raw_input('Enter a single number to be found in the list:\n')
    target = int(target_input)
    
    n = len(collection)
    print("Found at index:", 
            exponential_search(collection, n, target)); 

