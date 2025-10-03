

import pandas as pd
import numpy as np

# Care este evaluarea medie a produselor din magazinul online?
# Utilizați măsuri adecvate de tendință centrală.
df = pd.read_csv('online_store_data.csv')
def parse_rating(text):
    if pd.isna(text) or str(text).strip().lower() == "no value":
        return np.nan

    parts = str(text).split()
 
    try:
        return float(parts[0])
    except (ValueError, IndexError):
        return np.nan

df['rating'] = df['rating'].apply(parse_rating)
print(df['rating'].unique)

average_rating = df['rating'].mean()
print(f"Average book rating: {average_rating:.2f}")

# Care este cel mai frecvent brand din magazinul online?
# Utilizați măsuri adecvate de tendință centrală.

most_common_brand=df['brand'].mode()
print(f"Most common author: {", ".join(most_common_brand.astype(str))}")


# Care este cel mai vândut brand din magazinul online?
# Verificați numărul de produse vândute pentru fiecare dintre branduri. Brandul cu cele mai multe vânzări este cea mai bine vândută.


df['quantity_sold']=pd.to_numeric(df['quantity_sold'],errors='coerce').astype('Int32')
best_brand_stats = df.groupby('brand').agg({
    "quantity_sold": 'sum'
}).sort_values(by=["quantity_sold"],ascending=False).head(1)

print(best_brand_stats)

#  Care este evaluarea medie a produselor pe categorii?
# Presupune folosirea metodei adecvate de calcul a mediei aritmetice, peste coloana cu note, dar pentru fiecare categorie individual.

rating_per_category=df.groupby('category').agg({
    'rating': 'mean'
}).sort_values(by=['rating'],ascending=False)
print(rating_per_category)

# Cum arată popularitatea produselor în funcție de culori?
# Aceasta implică examinarea numărului de unități vândute în funcție de culoarea produsului. 
# Trebuie să afișați numărul total de produse vândute pentru fiecare dintre culori.


sell_item_with_colour=df.groupby('color').agg({
    'quantity_sold':'sum'
}).sort_values(by=['quantity_sold'],ascending=False)
print(sell_item_with_colour)

# Care sunt cele mai eficiente 5 branduri din punct de vedere al vânzărilor?
# Trebuie să găsiți cele mai eficiente 5 branduri din punct de vedere al vânzărilor. 
# Eficiența vânzărilor ar trebui măsurată prin raportul dintre numărul de bucăți vândute și numărul total de bucăți achiziționate.
# Numărul de bucăți achiziționate reprezintă suma unităților vândute și a celor care sunt încă în stoc. 
# Împărțirea numărului de unități vândute la suma dintre unitățile vândute și cele încă în stoc vă oferă eficiența unui brand. 
# Trebuie să folosiți aceste valori pentru a găsi cele mai eficiente 5 branduri.


df['quantity_in_stock']=pd.to_numeric(df['quantity_in_stock'],errors='coerce').astype('Int32')

top_brands=df.groupby('brand').agg(
    in_stoc=('quantity_in_stock','sum'),
    sold=('quantity_sold','sum')
)

top_brands['sold_ratio']=top_brands['sold']/(top_brands['in_stoc'] + top_brands['sold'])

print(top_brands.sort_values(by=['sold_ratio'],ascending=False).head(5))