# 2. Write a NumPy program to split the element of a given array with spaces. Sample Output:
# Original Array:
# ['Python PHP Java C++']
# Split the element of the said array with spaces:
# [list(['Python', 'PHP', 'Java', 'C++'])]
import numpy as np

newArray = np.array(input('Enter a string: ').split())

print(f'New Array: {newArray}')