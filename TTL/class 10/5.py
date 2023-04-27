# Show the car details as per buyers choice such as company, body-style, horsepower, average-
# mileage, price.
import pandas as pd

df = pd.read_csv('D:\codes\college\TTL\class 10\Automobile_data.csv')

company_name = input('Enter company: ')
body_style = input('Enter body-style: ')
horsepower = int(input('Enter minimum horsepower: '))
average_mileage = int(input('Enter minimum average-mileage: '))
price = int(input('Enter maximum price: '))
print('Car details as per buyers choice are:')
print(df[(df['company'] == company_name) & (df['body-style'] == body_style) & (df['horsepower'] > horsepower) & (df['average-mileage'] > average_mileage) & (df['price'] < price)])