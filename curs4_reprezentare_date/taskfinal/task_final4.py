


import numpy as np
import pandas as pd

df=pd.read_csv('online_store_data.csv')
# Care este diferența dintre cel mai bine și cel mai slab evaluat televizor?
# Utilizați intervalul (range = max - min)

#print(df['rating'].sort_values(ascending=False))

def parse_rating(text):
    if pd.isna(text) and str(text)=='no value':
        return np.nan
    
    parts=str(text).strip()
    try:
        return float(parts[0])
    except ValueError:
        return np.nan
df['rating']=df['rating'].apply(parse_rating)
df['category'] = df['category'].astype('category')

mask=df[df['category']=='TVs']
filter_df=mask.filter(items=['product_name','category','rating'])
sort_df = filter_df.sort_values(by=['rating'],ascending=False)

max_val = sort_df['rating'].max()
min_val = sort_df['rating'].min()
print(f"Max: {max_val}")
print(f"Min: {min_val}")
print(f'Range = {max_val-min_val}')


#  În ce interval de preț se află cel mai mare număr de telefoane mobile vândute?
# Calculați intervalul intercuartil (IQR)
print(df.dtypes)
print(df['category'].unique)
mask=df[df['category']=='Smartphones']
filter_df=mask.filter(items=['product_name','category','price','quantity_sold'])
sort_df=filter_df.sort_values(by=['price'],ascending=False)
print(sort_df)
Q1 = sort_df['price'].quantile(0.25)
Q3 = sort_df['price'].quantile(0.75)
IQR=Q3-Q1
print(f"{Q1:.2f} $ - {Q3:.2f} $ (IQR = {IQR:.2f} $)")

# Care sunt cele 5 branduri cu cele mai uniforme evaluări?
# Calculați abaterea standard a evaluărilor
df['brand'] = df['brand'].astype('category')
top_uniform_brands=df.groupby('brand',observed=True).agg(
    std_rating=('rating','std')
).sort_values(by=['std_rating'],ascending=False).head(5)

print(top_uniform_brands)

# Depinde numărul de evaluări de numărul de unități vândute? Mai multe unități vândute înseamnă mai multe evaluări sau invers?
# Împărțiți produsele în cuartile în funcție de numărul de evaluări

Q1=df['num_of_ratings'].quantile(.25)
Q2=df['num_of_ratings'].quantile(.5)
Q3=df['num_of_ratings'].quantile(.75)

def assigment_quantile(num_of_rating):
    if num_of_rating <= Q1:
        return '1st quantile'
    elif num_of_rating <= Q2:
        return '2nd quantile'
    elif num_of_rating <= Q3:
        return '3rd quantile'
    else:
        return '4th quantile'
    
df['quantile_rating']=df['num_of_ratings'].apply(assigment_quantile)
ranking_by_number_of_ratings=df.groupby('quantile_rating')['quantity_sold'].sum().reset_index
print(ranking_by_number_of_ratings)

