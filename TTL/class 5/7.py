# Write a program to create a 2D array with 1 on the border and 0 inside
import numpy as np

arr = np.ones((5, 5), dtype=int)
arr[1:-1, 1:-1] = 0
print(f'Array -> \n {arr}')
