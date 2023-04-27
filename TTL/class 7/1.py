# 1. Write a NumPy program to concatenate element-wise two arrays of string. Sample Output:
# Array1:
# ['Python' 'PHP']
# Array2:
# [' Java' ' C++']
# new array:
# ['Python Java' 'PHP C++']

import numpy as np

n = int(input('Enter size of each array: '))
arr1 = list(map(str, input('Enter all string of 1st array: ').split()))
arr1 = np.array(arr1)
arr2 = list(map(str, input('Enter all string of 2nd array: ').split()))
arr2 = np.array(arr2)
newArray = []
for i in range(n):
    newArray.append(arr1[i] + ' ' + arr2[i])
print(f'New Array: {newArray}')
