def main():
	n = int(input("Enter the number: "))
	for i in range(1, n + 1):
		b = checkarmstrong(i)
		if b:
			print(str(i) + " is an armstrong number")

