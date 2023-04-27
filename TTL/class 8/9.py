# Write a Pandas program to select the rows where the score is missing, i.e. is NaN.
import pandas as pd
import numpy as np

data = {
    'name': ['Alfred', 'Batman', 'Joker', 'Monkey', 'Cat'],
    'score': [np.nan, 12.8, 41.2, np.nan, 51.2],
    'attempts': [1, 5, 8, 3, 2],
    'qualify': ['yes', 'no', 'yes', 'no', 'no'],
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, columns=[
                  'name', 'score', 'attempts', 'qualify'], index=labels[:len(data['name'])])
print(df[df['score'].isnull()])
