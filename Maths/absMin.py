from abs import absVal
def absMin(x):
    """
    >>>absMin([0,5,1,11])
    0
    >>absMin([3,-10,-2])
    -2
    """
    j = absVal(x[0])
    for i in x:
        if absVal(i) < j: #if absolute value of x[i] is smaller than j, swap them
            j = i
    return j #finally, return the smallest absolute value in array X

def main():
    a = [1,2,-11]
    print(absMin(a)) # = 1

if __name__ == '__main__':
    main()
