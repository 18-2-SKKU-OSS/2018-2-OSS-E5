"""
이 코드는 Counting Sort를 파이썬으로 구현한 코드입니다.
    이름 그대로 숫자의 등장횟수를 세어줍니다.
    그 후 등장횟수+ 숫자의 누적합으로 정렬을 해줍니다.
    보시면 아시다시비 누적합 배열에 대한 접근을 달성하기 위해 엄청난 메모리를 낭비하게 됩니다.
"""

from __future__ import print_function


def counting_sort(collection):
    """
    Examples:
    >>> counting_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> counting_sort([])
    []
    >>> counting_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    # 배열이 비어있다면 반환해줍니다.
    if collection == []:
        return []

    # 입력받은 배열에 대한 정보를 얻어옵니다.
    coll_len = len(collection)
    coll_max = max(collection)
    coll_min = min(collection)

    # 수를 세는 새로운 배열을 만듭니다.
    counting_arr_length = coll_max + 1 - coll_min
    counting_arr = [0] * counting_arr_length

    # 입력에서 각자의 숫자가 얼마나 나타났는지 셈을 합니다.
    for number in collection:
        counting_arr[number - coll_min] += 1

    # 각 위치의 합은 그 과정동안의 합을 말해줍니다. 
    # 이제, counting_arr[i] 은 얼마나 많은 요소들은 i보다 작은 배열에 들어가 있는지 알수있습니다.
    for i in range(1, counting_arr_length):
        counting_arr[i] = counting_arr[i] + counting_arr[i-1]

    # 출력을 위한 배열을 만듭니다.
    ordered = [0] * coll_len

    # 이 과정에서 정렬이 됩니다.
    for i in reversed(range(0, coll_len)):
        ordered[counting_arr[collection[i] - coll_min]-1] = collection[i]
        counting_arr[collection[i] - coll_min] -= 1

    return ordered

def counting_sort_string(string):
    return ''.join([chr(i) for i in counting_sort([ord(c) for c in string])])


if __name__ == '__main__':
    # sordt_string 을 테스트 해보기 위한 코드입니다.
    assert "eghhiiinrsssttt" == counting_sort_string("thisisthestring")

    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(counting_sort(unsorted))
