# Print All audi Cars details and also sort them from lowest to highest price.
import pandas as pd

df = pd.read_csv('D:\codes\college\TTL\class 10\Automobile_data.csv')

print('All audi cars sorted from highest to lowest price are:')
print(df[df['company'] == 'audi'].sort_values(by='price', ascending=True))