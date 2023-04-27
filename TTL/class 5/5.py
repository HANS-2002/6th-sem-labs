# Write a program to concatenate element-wise two arrays of string
import numpy as np
arr1 = np.array(['a', 'b', 'c'])
arr2 = np.array(['d', 'e', 'f'])
print(f'Array -> {np.char.add(arr1,arr2)}')
