
import numpy as np
import pandas as pd
from preprocesing_data import prepare_data
data=pd.read_csv('books.csv')
df=prepare_data(data)

def find_negative_values(df, column_name):
    negative_values = df[(df[column_name] < 0)]
    return negative_values

ratings_count_negative = find_negative_values(df, "ratings_count")
print(ratings_count_negative.filter(items=['title', 'author', 'ratings_count']))

ratings_count_negative = find_negative_values(df, "price")
print(ratings_count_negative.filter(items=['title', 'author', 'price']))

ratings_count_negative = find_negative_values(df, "page_count")
print(ratings_count_negative.filter(items=['title', 'author', 'page_count']))

ratings_count_negative = find_negative_values(df, "dimensions_width")
print(ratings_count_negative.filter(items=['title', 'author', 'dimensions_width']))

ratings_count_negative = find_negative_values(df, "dimensions_thickness")
print(ratings_count_negative.filter(items=['title', 'author', 'dimensions_thickness']))

ratings_count_negative = find_negative_values(df, "dimensions_height")
print(ratings_count_negative.filter(items=['title', 'author', 'dimensions_height']))




mask = (df['ratings_count'].isna()) & (df['rating'].notna())
suspicious_values = df[mask]
print(suspicious_values.filter(items=['catalog_number', 'title', 'author', 'ratings_count', 'rating']))

df.loc[mask, 'rating'] = np.nan