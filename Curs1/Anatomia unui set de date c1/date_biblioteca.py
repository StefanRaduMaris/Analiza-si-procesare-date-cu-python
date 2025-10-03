

import pandas as pd
import csv

df_biblioteca = pd.read_csv("books.csv")
print(df_biblioteca.shape)
rows,columns =df_biblioteca.shape
df_biblioteca.columns = [col.lower().replace(' ', '_').replace('-', '_') for col in df_biblioteca.columns]
print(df_biblioteca.columns)
df_biblioteca.to_csv('books.csv',index=False,encoding='utf-8-sig')

