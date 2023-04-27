# Write a program to create a null vector of size 25 but the values from fifth to tenth elements are all 1
import numpy as np
arr = np.zeros(25, int)
for i in range(4, 11):
    arr[i] = 1
print(f'Array -> {arr}')