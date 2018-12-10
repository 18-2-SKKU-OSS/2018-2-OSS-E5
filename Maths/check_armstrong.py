def main():
	n = int(input("Enter the number: "))
	for i in range(1, n + 1):
		b = checkarmstrong(i)
		if b:
			print(str(i) + " is an armstrong number")

def checkarmstrong(n):
	t = n
	sum_num = 0
	while t != 0:
		r = t % 10
		
	
