

from preprocesing_data import prepare_data
import pandas as pd
import numpy as np


biblioteca=pd.read_csv('books.csv')
df=prepare_data(biblioteca)
print(df.dtypes)

sort_df=biblioteca.sort_values(by=['times_borrowed'],ascending=False)
shelf_width = 118
selected_books = []
current_width = 0.0

for idx, row in sort_df.iterrows():
    thickness = row['dimensions_thickness']
    if current_width + thickness <= shelf_width:
        selected_books.append(row)
        current_width += thickness
    if current_width >= shelf_width:
        break

selected_df = pd.DataFrame(selected_books).reset_index()

print("Width used:", current_width, "inches")
print(selected_df[['title', 'author', 'times_borrowed', 'dimensions_thickness']].to_string())
