

import pandas as pd

df=pd.read_csv("online_store_data.csv")
row,columns = df.shape
print(df.shape)
print(df.columns)

sorted_df=df.sort_values(by=['product_name','quantity_sold'],axis=0,ascending=False)
print(sorted_df.iloc[0])

mask=df[df['category']=='Smartphones']

sorted_smartphones=mask.sort_values(by=['product_name','quantity_sold'],ascending=[False,True])
print(sorted_smartphones.head(5).filter(items=['product_name','quantity_sold']))

mask_laptop=(df['category']=='Laptops') & (df['price'] > 0)
df_mask_laptop= df[mask_laptop]
sort_laptop = df_mask_laptop.sort_values(by=['price'],ascending=True).filter(items=['product_name','category','price'])

print(f'{sort_laptop.head(1).to_string()} \n')
print(f'{sort_laptop.tail(1).to_string()} \n')

## Varianta 2

reindex_laptop =sort_laptop.set_index('product_name')
row,columns=reindex_laptop.shape
print(f'Numarul de elemente este {row} \n')
print(f'{reindex_laptop.iloc[0]}\n')
print(f'{reindex_laptop.iloc[row-1]}\n')
