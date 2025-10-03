

import pandas as pd
from preprocesing_data import prepare_data

data = pd.read_csv('books.csv')
df = prepare_data(data)

genre_stats = df.groupby('genre', observed=True).agg(
    times_borrowed_std=('times_borrowed', 'std'),
    titles_count=('title', 'count')
)

genre_stats_filtered = genre_stats[genre_stats['titles_count'] >= 20]
genre_sorted = genre_stats_filtered.sort_values(by=["times_borrowed_std"])
print(genre_sorted)


section_stats = df.groupby('section', observed=True).agg(
    times_borrowed_std=('times_borrowed', 'std'),
    titles_count=('title', 'count')
)

section_stats_filtered = section_stats[section_stats['titles_count'] >= 20]
section_sorted = section_stats_filtered.sort_values(by=["times_borrowed_std"])
print(section_sorted)



Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1

iqr_books = df[(df['price'] >= Q1) & (df['price'] <= Q3)]

print(f"Price range of the middle 50% of books:")
print(f"{Q1:.2f} $ - {Q3:.2f} $ (IQR = {IQR:.2f} $)")
print(f"Total number of books: {len(iqr_books)}")


Q1 = df['times_borrowed'].quantile(0.25)
Q3 = df['times_borrowed'].quantile(0.75)
IQR = Q3 - Q1

iqr_books = df[(df['times_borrowed'] >= Q1) & (df['times_borrowed'] <= Q3)]

print(f"'Times borrowed' range of the middle 50% of books: {Q1} - {Q3}")
print(f"Total number of books: {len(iqr_books)}")
#influenteaza nr de pagini daca cartea e imprumutata mai des sau nu??

Q1 = df['page_count'].quantile(0.25)
Q2 = df['page_count'].quantile(0.50)
Q3 = df['page_count'].quantile(0.75)

def assign_quartile(pages):
    if pages <= Q1:
        return '1st quartile'
    elif pages <= Q2:
        return '2nd quartile'
    elif pages <= Q3:
        return '3rd quartile'
    else:
        return '4th quartile'

df['page_quartile'] = df['page_count'].apply(assign_quartile)

total_borrowed_per_quartile = df.groupby('page_quartile')['times_borrowed'].sum().reset_index()

print(total_borrowed_per_quartile)

 ##mini activitate influenteaza nr de pagini nota cartii?

Q1 = df['page_count'].quantile(0.25)
Q2 = df['page_count'].quantile(0.50)
Q3 = df['page_count'].quantile(0.75)

def assign_quartile(pages):
    if pages <= Q1:
        return '1st quartile'
    elif pages <= Q2:
        return '2nd quartile'
    elif pages <= Q3:
        return '3rd quartile'
    else:
        return '4th quartile'

df['page_quartile'] = df['page_count'].apply(assign_quartile)

rating_per_quartile = df.groupby('page_quartile')['rating'].mean().reset_index()

print(rating_per_quartile)