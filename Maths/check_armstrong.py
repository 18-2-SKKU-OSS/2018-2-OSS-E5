def main():
	n = int(input("Enter the number: ")) #input size of iteration
	for i in range(1, n + 1):
		b = checkarmstrong(i)
		if b:
			print(str(i) + " is an armstrong number")

def checkarmstrong(n):
	t = n
	sum_num = 0
	while t != 0:
		r = t % 10
		sum_num = sum_num + (r * r * r)
		t = t//10

	if sum_num == n:
		return True
	else:
		return False

if __name__ == '__main__':
	main()
