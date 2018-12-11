'''
이 코드는 파이썬으로 heap sort를 구현한 코드입니다.
힙 정렬이란 최대 힙 트리나 최소 힙 트리를  구성해 정렬을 하는 방법으로서,
내림차순 정렬을 위해서는 최대 힙을 구성하고 오름차순 정렬을 위해서는 최소 힙을 구성하면 된다.
최대 힙을 구성하여 정렬하는 방법은 아래와 같다.
    1.n개의 노드에 대한 완전 이진트리를 구성한다. 이때 루트노드부터 부노드, 왼쪽 자노드, 오른쪽 자노드순으로 구성한다.
    2.최대 힙을 구성한다. 최대 힙이란 부노드가 자노드보다 큰 트리를 말하는데, 
    단말 노드를 자노드로 가진 부노드부터 구성하며 아래부터 루트까지 올라오며 순차적으로 만들어 갈 수 있다.
    3.가장 큰 수(루트에 위치)를 가장 작은 수와 교환한다.
    4. 2와 3을 반복한다.
'''

from __future__ import print_function


def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted):
    '''
    Examples:
    >>> heap_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> heap_sort([])
    []

    >>> heap_sort([-2, -5, -45])
    [-45, -5, -2]
    '''
    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted

if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(heap_sort(unsorted))
