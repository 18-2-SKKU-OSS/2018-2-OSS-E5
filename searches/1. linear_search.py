"""
선형 탐색 (Linear Search)
리스트에서 특정한 값을 찾는 알고리즘 중 가장 간단한 알고리즘이다. 리스트에서 찾고자 하는 값을 맨 앞에서부터 
끝까지 차례대로 찾아 나간다. 검색할 리스트의 길이가 길면 비효율적이지만, 검색 방법 중 가장 단순하여 구현이 쉽고 
정렬되지 않은 리스트에서도 사용할 수 있다는 장점이 있다.
"""
from __future__ import print_function

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

#선형탐색
def linear_search(sequence, target):
    """
    :param sequence : 탐색을 진행할 배열
    :param target : 탐색할 키(key) 값
    ;return : 키 값이 있는 위치(index), 없을 경우 None

    예시:
    >>> linear_search([0, 5, 7, 10, 15], 0)
    0

    >>> linear_search([0, 5, 7, 10, 15], 15)
    4

    >>> linear_search([0, 5, 7, 10, 15], 5)
    1

    >>> linear_search([0, 5, 7, 10, 15], 6)

    """
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return None


if __name__ == '__main__':
    user_input = raw_input('Enter numbers separated by coma:\n').strip()
    sequence = [int(item) for item in user_input.split(',')]

    target_input = raw_input('Enter a single number to be found in the list:\n')
    target = int(target_input)
    result = linear_search(sequence, target)
    if result is not None:
        print('{} found at positions: {}'.format(target, result))
    else:
        print('Not found')
