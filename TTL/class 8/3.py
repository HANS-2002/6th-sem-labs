# Write a Pandas program to convert a NumPy array to a Pandas series.
import pandas as pd
import numpy as np

array = np.array([61, 23, 97, 27, 39])
print('Original array:', array)
print('Result series:\n', pd.Series(array))