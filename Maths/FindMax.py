#배열의 최대값을 찾는 알고리즘

def find_max(nums):
    max = nums[0]  #처음 원소부터 마지막 원소까지 비교
    for x in nums: 
      if x > max: #만약 max가 nums[x]보다 작을 경우, max를 num[x]로 변경
        max = x
    return max 

def main():
  print(find_max([2, 4, 9, 7, 19, 94, 5]))

if __name__ == '__main__':
  main()
