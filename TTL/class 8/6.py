# Write a Pandas program to create a dataframe from a dictionary and display it.
import pandas as pd

dictionary = {
    'a' : 1,
    'b' : 3,
    'c' : 9,
    'd' : 27,
    'e' : 81}

print('Original dictionary:', dictionary)
print('Result dataframe:')
print(pd.DataFrame(dictionary, index=[0]))