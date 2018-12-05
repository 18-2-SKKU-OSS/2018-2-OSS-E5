#2018-12-5 
#this fuction provide you a max value in array

def find_max(nums):
    max = nums[0]  #compare from the first element to the last element
    for x in nums: 
      if x > max: #if the max is smaller than nums[x], max is changed to num[x]
        max = x
    return max 

def main():
  print(find_max([2, 4, 9, 7, 19, 94, 5]))

if __name__ == '__main__':
  main()
