

import pandas as pd

df = pd.read_csv('ecommerce_orders_april.csv')

rows, columns = df.shape
#print(f"Dataset contains {rows} rows and {columns} columns.")
df.columns = [col.lower().replace(' ', '_').replace('--', '_').replace('__','_') for col in df.columns]
df.to_csv('ecommerce_orders_april.csv',index=False,encoding='utf-8-sig')
#print(df.columns)

# print(df.head(40))
# print(df.tail(0))

print(df.sample(n=5,random_state=42,replace=False))
print(df.iloc[0])

print(df.loc[2, "customer_name"])
print(df.at[2, "customer_name"])
print(df.to_string(columns=['customer_name', 'price']))
print(df.head(30).to_string(columns=['customer_name', 'price']))