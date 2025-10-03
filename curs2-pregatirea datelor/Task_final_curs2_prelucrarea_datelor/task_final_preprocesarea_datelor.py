
import numpy as np
import pandas as pd

data=pd.read_csv('online_store_data.csv')
def parse_rating(text):
    if pd.isna(text) or str(text).strip().lower() == "no value":
        return np.nan

    parts = str(text).split()
 
    try:
        return float(parts[0])
    except (ValueError, IndexError):
        return np.nan


# convertiți tipurile de coloane quantity_sold și num_of_ratings în valori întregi;
data['quantity_sold']=pd.to_numeric(data['quantity_sold'],errors='coerce').astype('Int32')
data['num_of_ratings']=pd.to_numeric(data['num_of_ratings'],errors='coerce').astype('Int32')
# convertiți tipul de coloană quantity_in_stock în valoare întreagă;
data['quantity_in_stock']=pd.to_numeric(data['quantity_in_stock'],errors='coerce').astype('Int32')
# convertiți tipul de coloană date_added în datetime;
data['date_added']=pd.to_datetime(data['date_added'],errors='coerce',format='%m_%d_%y')
# extrageți valorile numerice ale evaluărilor produselor din coloana rating;
#print(data.sort_values(by=['product_name','rating'],axis=0,ascending=True).filter(items=['product_name','rating']))
values = data[~data['rating'].str.contains('out of 10', case=False, na=False)]
data['rating'] = data['rating'].apply(parse_rating)
# eliminați rândurile care nu au valori din coloana product_name;
print(data['product_name'].isna().sum())
data.dropna(subset=['product_name'],how='all',inplace=True)
print(data['product_name'].isna().sum())

# eliminați rândurile care au valori lipsă în mai mult de 4 coloane;
print(data.shape)
data.dropna(axis=0,thresh=data.shape[1]-4,inplace=True)
print(data.shape)

# eliminați rândurile care sunt duplicate complete, păstrând doar primul rând și eliminând toate duplicatele ulterioare.
#print(data['rating'].value_counts)

total_duplicates = data.duplicated().sum()
print(total_duplicates)
data.drop_duplicates(keep='first', inplace=True, ignore_index=False)
total_duplicates = data.duplicated().sum()
print(total_duplicates)

#generați o caracteristică nouă care ar trebui să arate venitul realizat pe produs (revenue);
#venitul se calculează atunci când prețul produsului este înmulțit cu numărul total de exemplare vândute.
print(data.dtypes)
data['revenue'] = data['price']*data['quantity_sold']
print(data.sort_values(by=['product_name','revenue'],ascending=[False,True]).filter(items=['product_name','revenue']))


#Analiza
# găsiți cele 10 produse din categoria Keywords care au generat cel mai mare venit, 
# găsiți cele 10 produse din categoria TVs care au generat cel mai mic venit.

mask_k_df =data[data['category']=='Keyboards']

print(mask_k_df.sort_values(by=['revenue'],ascending=False).filter(items=['product_name','category','revenue']).head(10))

mask_tv_df =data[data['category']=='TVs']

print(mask_tv_df.sort_values(by=['revenue'],ascending=True).filter(items=['product_name','category','revenue']).head(10))