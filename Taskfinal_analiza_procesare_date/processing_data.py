

import pandas as pd
import numpy as np

df=pd.read_csv('fit_trackr_data.csv')

def convert_category(df):
    df['Gender']=df['Gender'].astype('category')
    df['Mood']=df['Mood'].astype('category')
    return df


def parse_duration_calories(text):
    if pd.isna(text) or str(text)=='no value':
        return np.nan
    parts=str(text).split()
    try :
        return float(parts[0])
    except:
        return np.nan
    
def convert_to_numeric(df):
    df['Duration']=df['Duration'].apply(parse_duration_calories)
    df['Calories']=df["Calories"].apply(parse_duration_calories)
    return df

def convert_to_date_time(df):
    df['Date']=pd.to_datetime(df['Date'],errors='coerce')
    return df

def deduplicate_data(df):
    df.drop_duplicates(keep='first', inplace=True, ignore_index=False)
    return df

def missing_values(df):
    df.dropna(axis=0,inplace =True)
    df.dropna(subset=['Username'], how='all', inplace=True)
    return df

def standardization_values(df):
    mapping={
        'Yoga':'yoga',
        'swim':'swimming',
        'swimm':'swimming',
        'Walking':'walking',
        'walk':'walking',
        'Walk':'walking'
    }
    df['Activity']=df['Activity'].astype(object).replace(mapping).astype('category')
    return df


def prepare_data(df):
    return df.pipe(convert_category).pipe(convert_to_numeric).pipe(convert_to_date_time).pipe(deduplicate_data).pipe(
        missing_values).pipe(standardization_values)

