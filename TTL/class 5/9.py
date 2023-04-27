# Write a program to extract all the contiguous 3x3 blocks from a random 10x10 matrix.
import numpy as np
arr = np.random.randint(0, 5, (10, 10))
print("Original array:")
print(arr)
(r, c) = arr.shape
print("\nAll 3x3 blocks:")
for i in range(r - 2):
    for j in range(c - 2):
        print(arr[i:i+3,j:j+3])
