import pandas as pd
import sys, os
sys.path.append('src')
from feature.pulizia_dati import pulisci_df, preprocessing

def get_data(path:str='dati\WA_Fn-UseC_-Telco-Customer-Churn.csv'):    
    # carico i dati dal csv contenuto nella rep locale
    df = pd.read_csv(path)
    # df = pulisci_df(df)
    df = preprocessing(df)
    return df

if __name__ == '__main__':
    print(get_data())