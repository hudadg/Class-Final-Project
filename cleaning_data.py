import pandas as pd 

def data_kredit():
    df = pd.read_csv('clean.csv')
    df.drop('Unnamed: 0',axis=1,inplace=True)
    return df
