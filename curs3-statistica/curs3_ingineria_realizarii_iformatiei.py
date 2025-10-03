

import pandas as pd
from preprocesing_data import prepare_data

data = pd.read_csv('books.csv')
df = prepare_data(data)

inventory_gap = df.groupby('section').agg({
    'title': 'count',
    'times_borrowed': 'sum'
})

inventory_gap['titles_to_borrow_ratio'] = inventory_gap['times_borrowed'] / inventory_gap['title']

print(inventory_gap.sort_values(by=['titles_to_borrow_ratio'], ascending=False))

#mini activitate 20 cei mai buni autori
author_group = df.groupby('author').agg({
    'times_borrowed':'sum',
    'title':'count'
})

author_group['borrow_to_title_ratio']=author_group['times_borrowed']/author_group['title']
print(author_group.sort_values(by=['borrow_to_title_ratio'],ascending = False).head(20))