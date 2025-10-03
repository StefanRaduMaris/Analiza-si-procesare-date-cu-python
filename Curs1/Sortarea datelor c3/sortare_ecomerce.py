

import pandas as pd

df=pd.read_csv('ecommerce_orders_april.csv')

print(df.columns)

sort_df=df.sort_values(by=['customer_name','product'],ascending=[True,False])

print(sort_df.head(20).to_string(columns=['customer_name', 'product',
       'category', 'quantity', 'price']))