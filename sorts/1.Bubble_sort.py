"""
파이썬으로 bubble sort를 구현한 코드입니다.
함수 bubble_sort:
    버블 소트라고 불리며
    두 인접한 원소를 검사하며 정렬하는 방법입니다.
    코드가 단순하기 때문에 자주 사용 됩니다.
"""    
from __future__ import print_function

def bubble_sort(collection):
    """
    Examples:
    >>> bubble_sort([0, 5, 4, 2, 2])
    [0, 2, 2, 4, 5]

    >>> bubble_sort([])
    []

    >>> bubble_sort([-2, -5, -45])
    [-45, -5, -2]
    
    >>> bubble_sort([-23,0,6,-4,34])
    [-23,-4,0,6,34]
    """
    length = len(collection)
    for i in range(length-1):
        swapped = False 
        for j in range(length-1-i):
            if collection[j] > collection[j+1]:
                swapped = True #인접한 원소를 비교후 배열에서 왼쪽의 원소가 더작을 경우 True 만들어준다
                collection[j], collection[j+1] = collection[j+1], collection[j]
        if not swapped: break  # 원소들이 이미 정렬되어있다면 종료한다.
    return collection


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3
    user_input = raw_input('Enter numbers separated by a comma:').strip() #콤마로 원소들을 구분한다.
    unsorted = [int(item) for item in user_input.split(',')]
    print(*bubble_sort(unsorted), sep=',')
