def absVal(num):
    """
    Function to fins absolute value of numbers.
    >>>absVal(-5)
    5
    >>>absVal(0)
    0
    """
    if num < 0:
        return -num #if the input number is negative, convert to positive
    else:
        return num #if the input number is positive, don't need to convert

def main():
    print(absVal(-34)) # = 34

if __name__ == '__main__':
    main()
