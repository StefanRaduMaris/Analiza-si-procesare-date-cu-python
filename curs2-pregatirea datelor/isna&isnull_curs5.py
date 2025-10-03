

import pandas as pd
from preprocesing_data import prepare_data 

data = pd.read_csv('online_shop_dataset.csv')

#print(data.shape)
row,columns=data.shape
data1=data.dropna(axis=1,thresh=row*0.5,inplace=False) 
biblioteca =pd.read_csv('books.csv')
df=prepare_data(biblioteca)

missing_count= df['author'].isna().sum()
print(missing_count)
df['author'] = df['author'].fillna("Unknown Author")






 