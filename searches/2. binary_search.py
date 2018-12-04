"""
이진 탐색 (Binary Search)
정렬된 리스트에서 특정 값의 위치를 찾는 알고리즘. 처음 중간의 값을 임의의 값으로 선택하여, 
그 값과 찾고자 하는 값의 크고 작음을 비교하는 방식을 채택하고 있다. 
처음 선택한 중앙값이 만약 찾는 값보다 크면 그 값은 새로운 최댓값이 되며, 작으면 그 값은 새로운 최솟값이 된다. 
검색 원리상 정렬된 리스트에만 사용할 수 있다는 단점이 있지만, 
검색이 반복될 때마다 목표값을 찾을 확률은 두 배가 되므로 속도가 빠르다는 장점이 있다.
"""
from __future__ import print_function
import bisect

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

#이진탐색알고리즘
def binary_search(sorted_collection, item):
    """
    input값은 반드시 정렬 된 채로 주어져야 합니다.
    그러지 않으면 원하지 않는 결과값이 나올 수 있습니다.
    :param sorted_collection : 탐색을 진행할 배열
    :param item : 탐색을 진행할 키(key) 값
    :return : 키 값이 있는 위치(index), 없을 경우 None
    
    예시:
    >>> binary_search([0, 5, 7, 10, 15], 0)
    0
    
    >>> binary_search([0, 5, 7, 10, 15], 15)
    4

    >>> binary_search([0, 5, 7, 10, 15], 5)
    1

    >>> binary_search([0, 5, 7, 10, 15], 6)

    """
    
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = (left + right) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        else:
            if item < current_item:
                right = midpoint - 1
            else:
                left = midpoint + 1
    return None

#라이브러리 내장함수를 이용한 이진탐색
def binary_search_std_lib(sorted_collection, item):
    
    index = bisect.bisect_left(sorted_collection, item)
    if index != len(sorted_collection) and sorted_collection[index] == item:
        return index
    return None

#재귀를 이용한 이진탐색
def binary_search_by_recursion(sorted_collection, item, left, right):
    """
    가장 처음 재귀는 left = 0, right=(len(sorted_collection)-1)을 초기값으로 줘야합니다.
    :param left : 탐색 범위의 시작
    :param right : 탐색 범위의 끝 
    """
    if (right < left):
        return None
    
    midpoint = left + (right - left) // 2

    if sorted_collection[midpoint] == item:
        return midpoint
    elif sorted_collection[midpoint] > item:
        return binary_search_by_recursion(sorted_collection, item, left, midpoint-1)
    else:
        return binary_search_by_recursion(sorted_collection, item, midpoint+1, right)

#입력값이 정렬이 됬는지 확인 해주는 함수
def __assert_sorted(collection):
    """
    :param collection : 입력 값
    ;return : 정렬이 되어있으면 True값 반환, 아니면 error 발생

    예시:
    >>> __assert_sorted([0, 1, 2, 4])
    True

    >>> __assert_sorted([10, -1, 5])
    error: Collection must be sorted!
    """
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
    result = binary_search(collection, target)
    if result is not None:
        print('{} binart search found at positions: {}'.format(target, result))
    else:
        print('Not found')
    
    #binary_search_std_lib 함수 사용
    result = binary_search_std_lib(collection, target)
    if result is not None:
        print('{} binart search by library found at positions: {}'.format(target, result))
    else:
        print('Not found')
    
    #binary_search_by_recursion 함수 사용
    result = binary_search_by_recursion(collection, target, 0, len(collection)-1)
    if result is not None:
        print('{} binary search by recursion found at positions: {}'.format(target, result))
    else:
        print('Not found')
