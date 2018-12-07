"""
이 코드는 파이썬으로 Merge Sort를 구현한 코드입니다.
병합 정렬이라고도 부르며 다음과 같이 작동합니다.
    1.리스트의 길이가 0또는 1이면 이미 정렬된 것으로 봅니다. 그렇지 않은 경우에는
    2.정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눕니다.
    3.각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬합니다.
    4.두 부분 리스트를 다시 하나의 정렬된 리스트로 합병합니다.
"""
from __future__ import print_function

# Merge Sort를 다른 방식으로 구현 하였으며 앞선 Merge_Sort 보다 좀더 빠르게 돌아가는 코드입니다.

def merge_sort(LIST):
    start = []
    end = []
    while len(LIST) > 1:
        a = min(LIST)
        b = max(LIST)
        start.append(a)
        end.append(b)
        LIST.remove(a)
        LIST.remove(b)
    if LIST: start.append(LIST[0])
    end.reverse()
    return (start + end)


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(merge_sort(unsorted))
