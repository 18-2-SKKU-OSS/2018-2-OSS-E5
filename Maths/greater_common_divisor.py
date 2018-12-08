# Greater Common Divisor - https://en.wikipedia.org/wiki/Greatest_common_divisor
# use Euclid method to calculate GCD
def gcd(a, b):
    return b if a == 0 else gcd(b % a, a)

def main():
    try:
        num1 = int(input("input first number: "))
	num2 = int(input("input second number: "))
	
    except (IndexError, UnboundLocalError, ValueError): #consider exception
        print("Wrong Input")
    print("GCD: ")
    print(gcd(num1, num2))

if __name__ == '__main__':
    main()

