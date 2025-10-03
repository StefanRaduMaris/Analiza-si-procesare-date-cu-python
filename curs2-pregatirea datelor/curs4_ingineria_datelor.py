

import pandas as pd

df=pd.read_csv('books.csv')
print(df['dimensions'].unique)

df[['dimensions_width', 'dimensions_thickness', 'dimensions_height']] = df['dimensions'].str.replace("inches", "").str.replace(" ", "").str.split('x', expand=True).astype(float)

df.drop('dimensions', axis=1, inplace=True)



df[['catalog_shelf', 'catalog_row', 'catalog_row_number']] = df['catalog_position'].str.split('-', expand=True)
print(df.filter(items=['title', 'catalog_shelf', 'catalog_row', 'catalog_row_number']).head(30))
df.drop('catalog_position',axis=1,inplace=True)


