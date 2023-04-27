# Write a program to create a vector with values ranging from 5 to 20 & reverse it
import numpy as np
arr = np.random.randint(5, 21, size = 10)
print(f'Original Array -> {arr}')
arr = np.flip(arr)
print(f'Reversed Array -> {arr}')