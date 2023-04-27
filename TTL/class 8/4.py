# Write a Pandas program to convert a given Series to an array.
import pandas as pd

series = pd.Series(['100', '200', 'python', '300.12', '400'])
print('Original series:\n', series)
print('Result array:', series.values)