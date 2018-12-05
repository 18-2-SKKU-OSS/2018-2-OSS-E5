def main():
    def findMin(x):
        minNum = x[0] #compare from the first element
        for i in x: #iterate i which travels 0 ~ max index
            if minNum > i: #if minNum is larger than x[i], swap them
                minNum = i
        return minNum

    print(findMin([0,1,2,3,4,5,-3,24,-56])) # = -56

if __name__ == '__main__':
    main()
