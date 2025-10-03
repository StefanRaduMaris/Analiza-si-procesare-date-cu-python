

import pandas as pd
from preprocesing_data import prepare_data

# data=pd.read_csv('books.csv')
# df=prepare_data(data)
# print(df[df.duplicated()])
# df.drop_duplicates(keep='first', inplace=True, ignore_index=False)
# print(df[df.duplicated()])


data1=pd.read_csv('online_shop_with_duplicates.csv')


total_duplicates = data1.duplicated().sum()
print(f"Total duplicates: {total_duplicates}")

print("Full duplicates: ")
print(data1[data1.duplicated()])

 #remove full duplicates
data1.drop_duplicates(keep='first', inplace=True, ignore_index=False)

# #check duplicates again...

total_duplicates = data1.duplicated().sum()
print(f"Total duplicates after deduplication: {total_duplicates}")