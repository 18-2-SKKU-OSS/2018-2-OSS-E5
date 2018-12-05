# 사용자가 제공 한 숫자의 계승을 찾는 파이썬 프로그램.

# 다른 결과에 대한 값 변경
num = 10

# 사용자로부터 입력을 받도록 하려면 아래의 주석 처리를 해제하십시오.
# num = int(input("Enter a number: "))

factorial = 1

# 숫자가 음수, 양수 또는 0인지 확인하십시오.
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
