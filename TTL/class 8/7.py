# Write a Pandas program to get the first 3 rows of a given DataFrame.
import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4, 5, 6],
                   'col2': [8, 9, 10, 11, 12, 13],
                   'col3': [14, 24, 34, 44, 54, 64],
                   'col4': [15, 25, 35, 45, 55, 65],
                   'col5': [16, 26, 36, 46, 56, 66],
                   'col6': [17, 27, 37, 47, 57, 67],
                   'col7': [18, 28, 38, 48, 58, 68],
                   'col8': [19, 29, 39, 49, 59, 69],
                   'col9': [10, 20, 30, 40, 50, 60]})

print('Original dataframe:')
print(df)
print('First 3 rows of the said dataframe:')
print(df.head(3))