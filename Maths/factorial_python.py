# 사용자가 제공 한 숫자의 계승을 찾는 파이썬 프로그램.

num = 1
factorial = 1
num = int(input("Enter a number: "))

# 숫자가 음수, 양수 또는 0인지 확인하십시오.
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
