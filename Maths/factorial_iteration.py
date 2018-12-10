"""Factorial of n (iterative implementation)."""

def factorial(n):
	 """Algorithm implementation."""

	r = 1

	while n > 0:

		r = r * n
		n--
		
	return r

n = int(input("Enter an integer n to compute its factorial: "))

print(str(n)+"! = "+str(factorial(n)))
