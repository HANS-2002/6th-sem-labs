# Find details of car with 4 number of cylinders with average mileage greater than 15
import pandas as pd

df = pd.read_csv('D:\codes\college\TTL\class 10\Automobile_data.csv')

print('Details of car with 4 number of cylinders with average mileage greater than 15 are:')
print(df[(df['num-of-cylinders'] == 'four') & (df['average-mileage'] > 15)])