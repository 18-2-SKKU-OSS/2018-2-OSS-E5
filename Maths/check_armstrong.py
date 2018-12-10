def main():
	n = int(input("Enter the number: ")) #input size of iteration
	for i in range(1, n + 1): #iteration
		b = checkarmstrong(i)
		if b: #if isArmstorng, print each number
			print(str(i) + " is an armstrong number")

def checkarmstrong(n):
	t = n
	sum_num = 0
	while t != 0:
		r = t % 10
		sum_num = sum_num + (r * r * r) #armstrong number rule
		t = t//10

	if sum_num == n: #check whether the result and original input number are equal
		return True
	else:
		return False

if __name__ == '__main__':
	main()
