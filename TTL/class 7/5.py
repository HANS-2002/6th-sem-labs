# 5. WAP to print max from axis 0 and min from axis 1 from the following 2-D array. Sample output:
# Printing Original array
# [[34 43 73]
# [82 22 12]
# [53 94 66]]

# Printing amin Of Axis 1
# [34 12 53]

# Printing amax Of Axis 0
# [82 94 73]
import numpy as np

arr = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

print('Printing Original array')
print(arr)

print(f'Printing amin Of Axis 1: {np.amin(arr, axis=1)}')

print(f'Printing amax Of Axis 0: {np.amax(arr, axis=0)}')