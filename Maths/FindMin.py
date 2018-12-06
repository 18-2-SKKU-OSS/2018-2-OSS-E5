def main():
    def findMin(x):
<<<<<<< HEAD
        minNum = x[0] #compare from the first element
        for i in x: #iterate i which travels 0 ~ max index
            if minNum > i: #if minNum is larger than x[i], swap them
=======
        minNum = x[0]
        for i in x:
            if minNum > i: #comparison 
>>>>>>> 5feb71f821f90c271d7bbfc20c1cef6d65ef49c3
                minNum = i
        return minNum

    print(findMin([0,1,2,3,4,5,-3,24,-56])) # = -56

if __name__ == '__main__':
    main()
