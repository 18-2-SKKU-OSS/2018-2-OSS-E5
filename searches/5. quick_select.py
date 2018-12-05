"""
K번째 숫자 탐색 (QuickSelect Search)
퀵 정렬을 참고하여 고안된 분할정복 탐색 알고리즘. 정렬이 되지 않은 리스트에서 k번째 작은 숫자를 찾는데 
효율적이다. 퀵 소트와 같이 피봇(pivot) 값을 설정하여 분할을 해서 문제를 해결한다. 평균 탐색 시간은 O(n)으로
효율적이나, 최악의 경우에는 O(n^2)으로 효율이 좋지 않다.
"""
import random

#분할
def _partition(data, pivot):
    """
    pivot 값보다 상대적으로 작거나 같거나 큰 
    3가지 배열로 분할을 한다. 
    :param data : 분할을 진행할 배열
    :param pivot : 피벗(pivot) 값
    ;return : 피벗 보다 작거나, 같거나 큰 3개의 배열
    """
    less, equal, greater = [], [], []
    for element in data:
        if element.address < pivot.address:
            less.append(element)
        elif element.address > pivot.address:
            greater.append(element)
        else:
            equal.append(element)
    return less, equal, greater
 
#퀵셀렉탐색
def quickSelect(list, k):
    """
     :param list : 탐색을 진행할 배열
     :param k : k 번째 작은 숫자 탐색
     ;return : 키 값이 있는 위치(index), 없을 경우 None
     """
    #k = len(list) // 정렬이 된 배열의 경우 k 값을 사용하여 중간값 구해서 피벗으로 사용
    smaller = []
    larger = []
    pivot = random.randint(0, len(list) - 1)
    pivot = list[pivot]
    count = 0
    smaller, equal, larger =_partition(list, pivot)
    count = len(equal)
    m = len(smaller)

    #k is the pivot
    if m <= k < m + count:
        return pivot
    # must be in smaller
    elif m > k:
        return quickSelect(smaller, k)
    #must be in larger
    else:
        return quickSelect(larger, k - (m + count))
