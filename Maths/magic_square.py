"""A magic square is an N×N grid of numbers in which the entries in each row, column and main diagonal sum to the same number (equal to N(N2+1)/2)"""


import numpy as np


print("Hi! Welcome to the magic square algorithm")
print("Please enter the number for which you would want a magic sqaure to be printed. Please enter an odd number")

# The odd number for which the magic square is created is stored in the variable N

N  = int(input())

# create a matrix with values 0 using numpy. The datatype is int for the elements in the matrix
magic_square = np.zeros((N,N), dtype=int)

n = 1
i, j = 0, N//2







