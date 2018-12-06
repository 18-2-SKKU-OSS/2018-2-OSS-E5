
from __future__ import print_function
import bisect

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

def exponentialSearch(arr, n, x):
    if (arr[0] == x): 
        return 0
  
    i = 1
    while (i < n and arr[i] <= x):
        i = i*2
  
    return binarySearch(arr, i//2, min(i, n), x)

def binarySearch(arr, l, r, x):
    if (r >= l) :
        mid = l + (r - l) // 2
    
        if (arr[mid] == x): 
            return mid
  
        if (arr[mid] > x) :
            return binarySearch(arr, l, mid-1, x)

        return binarySearch(arr, mid+1, r, x)
  
    return None

if __name__ == '__main__':
    import sys
    user_input = raw_input('Enter numbers separated by comma:\n').strip()
    collection = [int(item) for item in user_input.split(',')]
    
    target_input = raw_input('Enter a single number to be found in the list:\n')
    target = int(target_input)
    
    n = len(collection)
    print("Found at index:", 
            exponentialSearch(collection, n, target)); 

