from matplotlib.pyplot import get
import os
import pandas as pd
import feature.pulizia_dati as a

def get_data():
    # os.chdir('..\\')
    # from feature.pulizia_dati import pulisci_df
    df = pd.read_csv('../../data/WA_Fn-UseC_-Telco-Customer-Churn.csv')
    df = a.pulisci_df(df)
    return df

get_data()