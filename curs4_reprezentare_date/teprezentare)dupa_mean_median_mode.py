import pandas as pd
from preprocesing_data import prepare_data

data = pd.read_csv('books.csv')
df = prepare_data(data)

mean_val = df['times_borrowed'].mean()
median_val = df['times_borrowed'].median()
mode_val = df['times_borrowed'].mode()
max_val = df['times_borrowed'].max()
min_val = df['times_borrowed'].min()

print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Mode: {", ".join(mode_val.astype(str))}")
print(f"Max: {max_val}")
print(f"Min: {min_val}")

mean_val = df['rating'].mean()
median_val = df['rating'].median()
mode_val = df['rating'].mode()
max_val = df['rating'].max()
min_val = df['rating'].min()

print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Mode: {", ".join(mode_val.astype(str))}")
print(f"Max: {max_val}")
print(f"Min: {min_val}")

p01 = df['rating'].quantile(0.01)

bottom_1_percent_books = df[df['rating'] <= p01]

print(bottom_1_percent_books.filter(items=['title', 'rating']).sort_values(by=['rating'], ascending=False).to_string())

p95 = df['rating'].quantile(0.95)

top_5_percent_books = df[df['rating'] >= p95]

print(top_5_percent_books.filter(items=['title', 'rating']).sort_values(by=['rating'], ascending=False).to_string())


p99 = df['page_count'].quantile(0.99)

longest_1_percent = df[df['page_count'] >= p99]

print(longest_1_percent.filter(items=['title', 'page_count']).sort_values(by=['page_count'], ascending=False).to_string())
 