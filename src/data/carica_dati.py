import pandas as pd
import sys, os
sys.path.append('src')
from feature.pulizia_dati import pulisci_df

def get_data():    
    # carico i dati dal csv contenuto nella rep locale
    df = pd.read_csv('dati\WA_Fn-UseC_-Telco-Customer-Churn.csv')
    df = pulisci_df(df)
    return df

if __name__ == '__main__':
    print(get_data())