"""
파이썬으로 insertion sort를 구현한 코드입니다.
삽입 정렬 이라고 부르며 자료배열의 모든요소를 앞에서부터 차례대로 
이미 정렬된 배열 부분과 비교하여 자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘입니다.
배열이 길어질수록 효율이 떨어지지만, 구현이 간단하다는 장점이 있습니다.
"""
from __future__ import print_function


def insertion_sort(collection):
    """
    Examples:
    >>> insertion_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> insertion_sort([])
    []

    >>> insertion_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    for index in range(1, len(collection)):
        while index > 0 and collection[index - 1] > collection[index]: #index를 줄여가며 이미 정렬된 부분과 비교하며 위치를 찾고 
            collection[index], collection[index - 1] = collection[index - 1], collection[index] #찾은 위치에 삽입을 함으로써 정렬한다.
            index -= 1 

    return collection
if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(insertion_sort(unsorted))
