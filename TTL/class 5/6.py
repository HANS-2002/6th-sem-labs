# Write a program to create a 4x3 array with random values & find out the minimum & maximum values.
import numpy as np

arr = np.random.randint(1, 100, (4, 3), int)
print(f'Array -> \n {arr}')