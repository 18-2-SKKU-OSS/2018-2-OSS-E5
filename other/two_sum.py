"""
주어진 정수 배열을 이용하여 두 숫자의 인덱스를 반환하여 특정 대상에 합산합니다.

각 입력에는 정확히 하나의 솔루션이 있다고 가정 할 수 있으며 동일한 요소를 두 번 사용할 수 없습니다.

즉 여러 솔루션을 갖는 인자배열과 목표값을 사용하면 안됩니다.

예시:
인자 = [2, 7, 11, 15], 목표값 = 9,

nums[0] + nums[1] = 2 + 7 = 9 이므로,
return [0, 1].
"""

from __future__ import print_function

def twoSum(nums, target):
    """
    인자형: List[int]
    목표값의 형: int
    반환형: List[int]
    """
    chk_map = {}
    for index, val in enumerate(nums):
      compl = target - val
      if compl in chk_map: 
        indices = [chk_map[compl], index]
        print(indices)
        return [indices]
      else:
        chk_map[val] = index
    return False
