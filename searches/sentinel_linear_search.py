"""
선형 탐색 변형 (Sentinel Linear Search)
기존의 선형탐색의 변형된 탐색 알고리즘이다. 탐색을 진행하고자하는 배열의 끝에 타겟 값을 붙이고,
while 루프를 사용해 배열을 순차적으로 탐색을 하게 된다. 타겟 값이 있는 경우 while 문에서 빠져
나오게된다. while 문을 사용하기 때문에 기존의 선형탐색보다 N번 적은 비교횟수가 일어나게 된다.
"""
from __future__ import print_function

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

#선형탐색
def sentinel_linear_search(sequence, target):
    """
    :param sequence : 탐색을 진행할 배열
    :param target : 탐색할 키(key) 값
    ;return : 키 값이 있는 위치(index), 없을 경우 None
    """
    sequence.append(target)

    index = 0
    
    while sequence[index] != target:
        index += 1

    sequence.pop()

    if index == len(sequence):
        return None

    return index


if __name__ == '__main__':
    user_input = raw_input('Enter numbers separated by comma:\n').strip()
    sequence = [int(item) for item in user_input.split(',')]

    target_input = raw_input('Enter a single number to be found in the list:\n')
    target = int(target_input)
    result = sentinel_linear_search(sequence, target)
    if result is not None:
        print('{} found at positions: {}'.format(target, result))
    else:
        print('Not found')
