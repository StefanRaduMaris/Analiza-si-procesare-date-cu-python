import pandas as pd
from preprocesing_data import prepare_data

data = pd.read_csv('books.csv')

df = prepare_data(data)

# print(df['language'].unique())
# print(df['language'].value_counts())
# print(df['language'].cat.categories)

mapping = {
    'eng': 'en',
    'En': 'en',
    "pt-BR": "br",
    "zh-CN": "cn"
}
df['language'] = df['language'].astype(object).replace(mapping).astype("category")
# print(df['language'].value_counts())


print(df['section'].value_counts())
mapping = {
    'Young Adult (YA)': 'Young Adult',
    "Children's": "Children",
    "Children's Fiction": "Children"
}
df['section'] = df['section'].astype(object).replace(mapping).astype("category")
print(df['section'].value_counts())