# Write a program to create a 4x4 matrix with values 1,2,3 just below & above the diagonal, rest zeros.
import numpy as np

arr = np.zeros((4, 4), int)
np.fill_diagonal(arr[1:], [1, 2, 3])
np.fill_diagonal(arr[:, 1:], [1, 2, 3])
print(f'Array -> \n')
for i in arr:
    for j in i:
        print(j, end=' ')
    print('')
