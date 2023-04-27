# WAP to check if a given 2D matrix is magical
import numpy as np

arr = np.array([[17, 24, 1, 8, 15],
                [23, 5, 7, 14, 16],
                [4, 6, 13, 20, 22],
                [10, 12, 19, 21, 3],
                [11, 18, 25, 2, 9]])


def isMagic(a):
    rows = [np.sum(a[0:1]), np.sum(a[1:2]), np.sum(
        a[2:3]), np.sum(a[3:4]), np.sum(a[4:5])]
    cols = [np.sum(a[:, 0:1]), np.sum(a[:, 1:2]), np.sum(
        a[:, 2:3]), np.sum(a[:, 3:4]), np.sum(a[:, 4:5])]
    diag1 = np.sum(np.diagonal(a))
    np.fliplr(a)
    diag2 = np.sum(np.diagonal(a))
    vals = set([np.max(rows), np.min(rows),
                np.max(cols), np.min(cols), diag1, diag2])
    if len(vals) == 1:
        return True
    return False


print(f'Given Matrix:')
print(arr)
if isMagic(arr):
    print('Matrix is magical')
else:
    print('Matrix is not magical')
