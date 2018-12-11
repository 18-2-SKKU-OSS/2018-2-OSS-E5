def findMin(nums):
    min = nums[0]  #처음 원소부터 마지막 원소까지 비교
    for x in nums: 
      if x < min: #만약 max가 nums[x]보다 클 경우, max를 num[x]로 변경
        min = x
    return min 

def main(): 
    print(findMin([0,1,2,3,4,5,-3,24,-56])) # min = -56

if __name__ == '__main__':
    main()
