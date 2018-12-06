
from __future__ import print_function
import bisect

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

#피보나치 탐색
def fibonacci_search(arr, x, n):
    fibMMm2 = 0;   # (m-2)'th Fibonacci No. 
    fibMMm1 = 1;   # (m-1)'th Fibonacci No. 
    fibM = fibMMm2 + fibMMm1;  # m'th Fibonacci

    while (fibM < n): 
        fibMMm2 = fibMMm1; 
        fibMMm1 = fibM; 
        fibM  = fibMMm2 + fibMMm1; 
  
    offset = -1; 
  
 
    while (fibM > 1):
        i = min(offset+fibMMm2, n-1); 
  
        if (arr[i] < x):
            fibM  = fibMMm1; 
            fibMMm1 = fibMMm2; 
            fibMMm2 = fibM - fibMMm1; 
            offset = i; 
        elif (arr[i] > x):
            fibM  = fibMMm2; 
            fibMMm1 = fibMMm1 - fibMMm2; 
            fibMMm2 = fibM - fibMMm1; 
        else:
            return i; 
  

    if(fibMMm1 and arr[offset+1]==x):
        return offset+1; 
  
    return -1; 

if __name__ == '__main__':
    import sys
    user_input = raw_input('Enter numbers separated by comma:\n').strip()
    collection = [int(item) for item in user_input.split(',')]
    
    target_input = raw_input('Enter a single number to be found in the list:\n')
    target = int(target_input)
    
    n = len(collection)
    x = 85; 
    print("Found at index:", 
            fibonacci_search(collection, target, n)); 

