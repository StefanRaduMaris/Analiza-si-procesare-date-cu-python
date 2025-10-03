

import pandas as pd
from preprocesing_data import prepare_data

data = pd.read_csv('books.csv')
df = prepare_data(data)

std_year = df['year_published'].std()
mean_year = df['year_published'].mean()

print(std_year)
print(mean_year)

std_times_borrowed = df['times_borrowed'].std()
mean_times_borrowed = df['times_borrowed'].mean()

print(std_times_borrowed)
print(mean_times_borrowed)

sd = df['times_borrowed'].std()
q1 = df['times_borrowed'].quantile(0.25)
q3 = df['times_borrowed'].quantile(0.75)
iqr = q3 - q1
print(f"Standard deviation: {sd:.2f}")
print(f"IQR (Q3 - Q1): {iqr:.2f}")

#Mini activitate

sd = df['rating'].std()
q1 = df['rating'].quantile(0.25)
q3 = df['rating'].quantile(0.75)
iqr = q3 - q1

print(f"Standard deviation: {sd:.2f}")
print(f"IQR (Q3 - Q1): {iqr:.2f}")