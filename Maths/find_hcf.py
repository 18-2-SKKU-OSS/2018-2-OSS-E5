# Program to find the HCF of two Numbers
def find_hcf(num_1, num_2):
    if num_1 == 0: #exception case
        return num_2
    if num_2 == 0: #exception case
        return num_1
    # Base Case
    if num_1 == num_2: #if two numbers are equal
        return num_1
    if num_1 > num_2: #if num1 is larger than num2, recursively function call
        return find_hcf(num_1 - num_2, num_2)
    return find_hcf(num_1, num_2 - num_1)


def main():
    num_1 = int(input("input number 1: "))
    num_2 = int(input("input number 2: "))
    print('HCF of %s and %s is %s:' % (num_1, num_2, find_hcf(num_1, num_2)))


if __name__ == '__main__':
    main()
