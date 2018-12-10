"""
이 코드는 파이썬으로 Quick Sort를 구현한 코드입니다.
퀵 정렬은 divide and conquer 방법을 통해 리스트를 정렬합니다.
    1.리스트를 가운데서 하나의 원소를 고른다. 이렇게 고른 원소를 pivot이라고 한다.
    2.pivot 앞에는 pivot 보다 값이 작은 모든 원소들이 오고, pivot 뒤에는 pivot 보다 값이 큰 모든 원소들이 오도록 pivot을 기준으로 리스트를 둘로
    나눈다. 이렇게 리스트를 둘로 나누는 것을 partition이라고 한다. partition을 마친 뒤에 pivot이 더 이상 움직이지 않는다.
    3.분할된 두 개의 작은 리스트에 대해 재귀적으로 이 과정을 반복한다. 재귀는 리스트의 크기가 0이나 1이 될 때까지 반복된다.
"""
from __future__ import print_function


def quick_sort(ARRAY):
    """
    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> quick_sort([])
    []

    >>> quick_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    ARRAY_LENGTH = len(ARRAY)
    if( ARRAY_LENGTH <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        GREATER = [ element for element in ARRAY[1:] if element > PIVOT ]
        LESSER = [ element for element in ARRAY[1:] if element <= PIVOT ]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [ int(item) for item in user_input.split(',') ]
    print( quick_sort(unsorted) )
