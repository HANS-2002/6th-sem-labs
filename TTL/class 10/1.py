# From the given dataset print the first and last five rows.
import pandas as pd

df = pd.read_csv('D:\codes\college\TTL\class 10\Automobile_data.csv')

print('First five rows are:')
print(df.head(5))

print('Last five rows are:')
print(df.tail(5))