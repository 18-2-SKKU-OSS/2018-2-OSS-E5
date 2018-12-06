"""
파이썬으로 selection sort를 구현한 코드입니다
함수 selection_sort:
	선택정렬이라고 불리며
	1.주어진 리스트 중 최소값을 찾는다
	2. 그 값을 맨 앞에 위치한 값과 교체한다
	3.맨처음 위치를 뺀 나머지 리스트를 같은 방법으로 교체한다.
"""
from __future__ import print_function


def selection_sort(collection):
    """
    Examples:
    >>> selection_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> selection_sort([])
    []

    >>> selection_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    length = len(collection)
    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if collection[k] < collection[least]:
                least = k
        collection[least], collection[i] = (
            collection[i], collection[least]
        )
    return collection


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3
    for i in range(3): 
        user_input = raw_input('Enter numbers separated by a comma:\n').strip()
        unsorted = [int(item) for item in user_input.split(',')]
        print(selection_sort(unsorted))
