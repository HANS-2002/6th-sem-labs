# 4. Write a NumPy program to count a given word in each row of a given array of string values. Sample output:
# Original array of string values:
# [['Python' 'NumPy' 'Exercises']
# ['Python' 'Pandas' 'Exercises']
# ['Python' 'Machine learning' 'Python']]
# Count 'Python' row wise in the above array of string values:
# [[1 0 0]
# [1 0 0]
# [1 0 1]]

import numpy as np

arr = np.array([['Python is Python', 'NumPy', 'Exercises'], 
                ['Python', 'Pandas', 'Exercises'], 
                ['Python', 'Machine learning', 'Python']])
print('Original array of string values: ')
print(arr)
count = []
for lis in arr:
    cnt = []
    for sent in lis:
        cnt.append(sent.count('Python'))
    count.append(cnt)
print('Counting python in each row: ')
for i in count:
    print(i)
