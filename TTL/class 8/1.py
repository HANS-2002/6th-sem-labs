# Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
import pandas as pd

series1 = pd.Series([12, 41, 16, 81, 10])
series2 = pd.Series([51, 33, 65, 97, 29])
print("Original Series:")
print(series1)
print(series2)
print("Add two Series:", (series1 + series2))
print("Subtract two Series:", (series1 - series2))
print("Multiply two Series:", (series1 * series2))
print("Divide Series1 by Series2:", (series1 / series2))
