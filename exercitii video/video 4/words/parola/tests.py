from django.test import TestCase
import pandas as pd
# Create your tests here.


with open('parole.csv','w') as file_writer:
    file_writer.write('parole')

df = pd.read_csv('parole.csv')

print(df)
df.to_json('parole.json')