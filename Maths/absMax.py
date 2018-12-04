from abs import absVal
def absMax(x):
    """
    >>>absMax([0,5,1,11])
    11
    >>absMax([3,-10,-2])
    -10
    """
    j = x[0]#compare from the first element to the last one

    for i in x:
        if absVal(i) > j:#if absolute value of x[i] is smaller than absolute Max value, swap them
            j = i
    return j
    #BUG: i is apparently a list, TypeError: '<' not supported between instances of 'list' and 'int' in absVal


def main():
    a = [1,2,-11]
    print(absMax(a)) #

if __name__ == '__main__':
    main()
