# Write a Pandas program to convert a dictionary to a Pandas series.
import pandas as pd

dictionary = {
    'a' : 1, 
    'b' : 3,
    'c' : 9, 
    'd' : 27,
    'e' : 81}

print('Original dictionary:', dictionary)
print('Result series:\n', pd.Series(dictionary))