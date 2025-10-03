

import pandas as pd
from preprocesing_data import prepare_data

data = pd.read_csv('books.csv')
df = prepare_data(data)

#print(df.describe(include='all'))
average_price = df["price"].mean()
print(f"Average book price: ${average_price:.2f}")

median_price = df["price"].median()
print(f"Median book price: ${median_price:.2f}")

average_page_count = df["page_count"].mean()
print(f"Average amount of pages per book: {average_page_count:.2f}")

median_price = df["page_count"].median()
print(f"Median amount of pages per book :{median_price:.2f}")

genre_mode = df["genre"].mode()
print(f"Genre mode: {", ".join(genre_mode.astype(str))}")

most_common_authors = df["author"].mode()
print(f"Most common author: {", ".join(most_common_authors.astype(str))}")