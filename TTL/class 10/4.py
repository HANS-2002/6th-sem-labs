# Find the average mileage of each car making company.
import pandas as pd

df = pd.read_csv('D:\codes\college\TTL\class 10\Automobile_data.csv')

print('Average mileage of each car making company is:')
print(df.groupby('company')['average-mileage'].mean())