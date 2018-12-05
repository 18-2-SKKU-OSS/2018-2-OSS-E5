"""
보간 탐색 (Interpolation Search)
이진 탐색의 비효율성을 개선시킨 알고리즘이다. 이진 탐색의 경우 찾는 대상이 어디에 위치하건
일관되게 반씩 줄여가며 탐색을 진행한다. 반면 보간 탐색은 타겟이 상대적으로 앞에 위치한다고
판단을 하면 앞쪽에서 탐색을 진행한다. 따라서, 찾는 데이터와 가깝기 때문에 이진 탐색보다
속도가 뛰어나다.
"""
from __future__ import print_function

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

#보간탐색
def interpolation_search(sorted_collection, item):
    """
    input값은 반드시 정렬 된 채로 주어져야 합니다.
    그러지 않으면 원하지 않는 결과값이 나올 수 있습니다.
    :param sorted_collection: 탐색을 진행할 정렬된 배열
    :param item : 탐색을 진행할 키(key) 값
    ;return : 키 값이 있는 위치(index), 없을 경우 None
    """
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        point = left + ((item - sorted_collection[left]) * (right - left)) // (sorted_collection[right] - sorted_collection[left])
        
        #out of range check
        if point<0 or point>=len(sorted_collection):
            return None

        current_item = sorted_collection[point]
        if current_item == item:
            return point
        else:
            if item < current_item:
                right = point - 1
            else:
                left = point + 1
    return None

#재귀를 이용한 보간탐색
def interpolation_search_by_recursion(sorted_collection, item, left, right):
    """
    가장 처음 재귀는 left = 0, right=(len(sorted_collection)-1)을 초기값으로 줘야합니다.
    :param left : 탐색 범위의 시작
    :param right : 탐색 범위의 끝 
    """
    point = left + ((item - sorted_collection[left]) * (right - left)) // (sorted_collection[right] - sorted_collection[left])

    #out of range check
    if point<0 or point>=len(sorted_collection):
        return None

    if sorted_collection[point] == item:
        return point
    elif sorted_collection[point] > item:
        return interpolation_search_by_recursion(sorted_collection, item, left, point-1)
    else:
        return interpolation_search_by_recursion(sorted_collection, item, point+1, right)

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
        sys.exit('Sequence must be sorted to apply interpolation search')

    target_input = raw_input('Enter a single number to be found in the list:\n')
    target = int(target_input)
    
    #interpolation_search 함수 사용
    result = interpolation_search(collection, target)
    if result is not None:
        print('{} interpolation search found at positions: {}'.format(target, result))
    else:
        print('Not found')
        
    #interpolation_search_by_recursion 함수 사용
    result = interpolation_search_by_recursion(collection, target, 0, len(collection)-1)
    if result is not None:
        print('{} interpolation search by recursion found at positions: {}'.format(target, result))
    else:
        print('Not found')
