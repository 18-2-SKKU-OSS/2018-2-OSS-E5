#implementation modular exponentation
#this fuction calculate value of base^power % mod
def modularExponential(base, power, mod):
	if power < 0:
		return -1
	base %= mod
	result = 1

	while power > 0:
		if power & 1:
			result = (result * base) % mod
		power = power >> 1
		base = (base * base) % mod
	return result


def main():
	
	base = int(input("input base: "))
	power = int(input("input power: "))
	mod = int(input("input mod: "))
	
	print(modularExponential(base, power, mod))


if __name__ == '__main__':
	main()
