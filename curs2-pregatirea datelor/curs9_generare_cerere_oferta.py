

import pandas as pd
from preprocesing_data import prepare_data

data = pd.read_csv('books.csv')
df = prepare_data(data)

df['borrowings_per_copy'] = df['times_borrowed'] / df['total_copies']
sorted_df = df.sort_values(by='borrowings_per_copy', ascending=False)
top_50 = sorted_df.head(50)

print(top_50[['title', 'times_borrowed', 'total_copies', 'borrowings_per_copy']])


df = df[df['section'] != 'Rare Books']

df['borrowings_per_copy'] = df['times_borrowed'] / df['total_copies']
sorted_df = df.sort_values(by='borrowings_per_copy')
top_50 = sorted_df.head(50)

print(top_50[['title', 'times_borrowed', 'total_copies', 'borrowings_per_copy']])