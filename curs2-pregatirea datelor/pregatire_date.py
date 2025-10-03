

import pandas as pd

df=pd.read_csv('books.csv')

print(df.dtypes)
print(df.info())

df['times_borrowed']= df['times_borrowed'].astype('Int32')
df['page_count']=df['page_count'].astype('Int32')
df['total_copies']=pd.to_numeric(df['total_copies'],errors='coerce')


mask=(df['genre'] =='Science')&(df['total_copies'] < 4)
df_mask = df[mask]
sort_df=df_mask.sort_values(by=['genre'],axis=0,ascending=True).filter(items=['title','genre','total_copies'])
#print(sort_df.head(10))

df['year_published'] = pd.to_numeric(df['year_published'],errors='coerce')
df['year_published']=df['year_published'].astype('Int32')

mask = (df['year_published'] > 1960) & (df['year_published']<1970)
df_mask = df[mask] 
sort_mask = df_mask.sort_values(by=['year_published'],ascending=True)

#print(sort_mask.filter(items=['title','year_published']))


df['last_borrowed_date']=pd.to_datetime(df['last_borrowed_date'],format='%d_%b_%y',errors='coerce')

print(df.info())

sort_df =df.sort_values(by=['title','last_borrowed_date'],ascending=[False,True])
print(sort_df.head(10).filter(items=['title','last_borrowed_date']))




df = pd.read_csv('books.csv')

df['last_borrowed_date'] = pd.to_datetime(df['last_borrowed_date'], format='%d_%b_%y', errors='coerce')

data = {
    'years': df['last_borrowed_date'].dt.year,
    'months': df['last_borrowed_date'].dt.month,
    'days': df['last_borrowed_date'].dt.day
}

new_df = pd.DataFrame(data=data, dtype='Int32')

print(new_df)

df=pd.read_csv('books.csv')
print(df.info())
df['last_borrowed_date']=pd.to_datetime(df['last_borrowed_date'],errors='coerce',format='%d_%b_%y')
mask = (df['last_borrowed_date'].dt.year == 2024) & (df['last_borrowed_date'].dt.month == 12)
df_mask=df[mask]
print(df_mask.filter(items=['title','last_borrowed_date']))

print(df.nunique())
print(df['section'].value_counts())
df['genre'] = df['genre'].astype('category')
df['section'] = df['section'].astype('category')
df['language'] = df['language'].astype('category')
print(df.memory_usage(deep=True))