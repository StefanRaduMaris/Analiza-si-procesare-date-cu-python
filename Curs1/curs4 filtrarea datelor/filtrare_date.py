

import pandas as pd

df=pd.read_csv("books.csv")

#filtrare dupa structura
filter_df=df.filter(items=['title','author'])
print(filter_df.head(20))

print(df.columns)

filter_df2=df.filter(items=['title','author','year_published'])
print(filter_df2.tail(10))


#filtrare dupa randuri
#e la fel ca filtrarea dupa structura si introducem parametrul axis
#vom numerota coloanele si nu le vom mai numi 'title etc
#in items avem randurile pe care vrem sa le afisam
filter_df3=df.filter(items=[1,2,3,4],axis=0)
print(filter_df3)
print(df.iloc[12])

#filtrarea dupa randuri sau coloane se numeste filtrare structurata

#filtrarea dupa identitate folosind like

filter_df4=df.set_index('catalog_position')
filter_like=filter_df4.filter(like='A1-B1',axis=0)
print(filter_like)

#concatenarea filtrarii, filtram dupa mai multe filtre
print("Verifica mesajul")
filter_df4=df.set_index('catalog_position')
filter_concat = filter_df4.filter(like='A1-B1',axis=0).filter(items=['title','author'])
print(filter_concat.head(5).to_string())


filter5=filter_df4.filter(like='A2',axis=0).filter(items=['title','page_count'])
print(filter5.tail(5).to_string())

##filtrarea dupa valori!!!!

author_filter=df[df['author']=='Mark Twain']
print(author_filter)


print(df.columns)

genre_mask=df[df['genre']== 'Horror']
print(genre_mask.filter(items=['title','genre']))

print(f'Avem {genre_mask.shape[0]} carti cu acest gen')

##Filtrarea dupa mai multe valori

mask = df[df['genre'] =='Science' ]
sort_df=mask.sort_values(by='times_borrowed',ascending=False).filter(items=['title','times_borrowed'])
print(sort_df.head(1).to_string())

#varianta2
mask = (df['genre'] == 'Science')
science_books_sorted = df[mask].sort_values(by='times_borrowed', ascending=False)
print(science_books_sorted.filter(items=['title', 'author', 'times_borrowed']).iloc[0])

 