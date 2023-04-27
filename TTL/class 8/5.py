# Write a Pandas program to convert Series of lists to one Series.
import pandas as pd

seriesOfList = pd.Series([[12, 45, 67, 91], [-3, -2, -6, -11, -31], ['a', 'b', 'e'], ["hans", "peter"]])
print('Original series of lists:\n', seriesOfList)
print('Ans series:\n', pd.Series(seriesOfList.sum()))
