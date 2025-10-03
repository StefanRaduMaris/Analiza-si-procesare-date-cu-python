

import pandas as pd
from processing_data import prepare_data
import matplotlib.pyplot as plt

data=pd.read_csv('fit_trackr_data.csv')
df=prepare_data(data)
df.to_csv("date_procesate.csv", index=False, encoding="utf-8")

#Care este durata medie a activității?
avg_duration_df = df['Duration'].mean()
print(f"Average exercises dutation: {avg_duration_df:.2f}")

# Ce tip de activitate practică cel mai des utilizatorii?
print(df['Activity'].value_counts().head(1))

# Care este cea mai frecventă stare de spirit a utilizatorului după activitate?
print(df['Mood'].value_counts().head(1))

#  Care este variația consumului de calorii în funcție de tipul de activitate?
std_calories=df.groupby('Activity').agg(
    Calories_std=('Calories','std'),
    Calories_mean=('Calories','mean')
).sort_values(by=['Calories_std'],ascending=False)
print(std_calories)

# Care este diferența între vârstele utilizatorilor față de 50% din mijlocul datelor?

Q1 = df['Age'].quantile(0.25)
Q2 = df['Age'].quantile(0.5)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

iqr_age = df[(df['Age'] >= Q1) & (df['Age'] <= Q3)]

print(f"The difference between range of the middle 50% of age : {Q1} - {Q3}")
print(f'The 50 % quartile is {Q2}')
print(f"Total number of users {len(iqr_age)}")

# Ce tipuri de activități determină în cea mai fericită dispoziție?
mask=df[df['Mood']=='Happy']
print(mask)
the_happiest_activity=mask.groupby('Activity').agg({
    'Mood':'count'
}).sort_values(by=['Mood'],ascending = False)

print(the_happiest_activity)

# Utilizatorii cu activități mai lungi au o dispoziție mai fericită?
Q1=df['Duration'].quantile(.25)
Q2=df['Duration'].quantile(.5)
Q3=df['Duration'].quantile(.75)

def assigement_time(duration):
    if duration <=Q1:
        return "short period"
    elif duration <=Q2:
        return "medium period"
    elif duration <=Q3:
        return "long period"
    else:
        return "really long period"

mask=df[df['Mood']=='Happy']
df['Duration_quantile']=mask['Duration'].apply(assigement_time)
time_quantile=df.groupby('Duration_quantile')['Mood'].count()
print(time_quantile)
