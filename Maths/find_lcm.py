#find least common multiple

def find_lcm(num_1, num_2):
    max = num_1 if num_1 > num_2 else num_2
    
    while (True): #find least common multiple counting max by one and checking whether it is lcm or not
        if ((max % num_1 == 0) and (max % num_2 == 0)):
            break
        max += 1
    return max


def main():
    num_1 = int(input("input number 1: "))
    num_2 = int(input("input number 2: "))
    print(find_lcm(num_1, num_2))


if __name__ == '__main__':
    main()
