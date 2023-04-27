# Write a program to create a vector with 10 random values & sort first half ascending & second half descending.
import numpy as np

arr = np.random.randint(1, 100, size=10)
print(f'Original Array -> {arr}')
firstHalf = np.sort(arr[:5])
secondHalf = np.sort(arr[5:])[::-1]
arr = np.concatenate((firstHalf, secondHalf))
print(f'Flip Sorted Array -> {arr}')
