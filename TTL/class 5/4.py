# Write a program to create a vector of size 10 with values ranging from 0 to 1, both excluded.
import numpy as np
arr = np.linspace(0, 1, 12)[1: -1]
print(f'Array -> {arr}')
