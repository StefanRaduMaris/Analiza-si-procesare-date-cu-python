

import pandas as pd

df = pd.read_csv('books.csv')
df.sort_values(by="title", inplace=True)
print(df.head(2).to_string(columns=['title', 'author']))


print(df.columns)
sorted_df = df.sort_values(by="year_published")
print(sorted_df.head(3).to_string(columns=['title', 'author', 'year_published']))


borrow_time_df=df.sort_values(by='times_borrowed',ascending=False)
print(borrow_time_df.head(5).to_string(columns=['title','times_borrowed']))

min_page=df.sort_values(by='page_count',ascending=True)
max_page=df.sort_values(by='page_count',ascending=False)
print(min_page.head(1).to_string(columns=['title','page_count']))
print(max_page.head(1).to_string(columns=['title','page_count']))