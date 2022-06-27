import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder


def pulisci_df(df):
    # elimino i dati null e definisco il tipo della colonna
    df = df.drop(df[df['TotalCharges'] == ' '].index)
    df.TotalCharges = df['TotalCharges'].astype(float)
    
    # utilizzo la label encorder per le colonne object
    df = df.apply(LabelEncoder().fit_transform)

    # scaler delle colonne continue
    scaler = MinMaxScaler()
    tenure = scaler.fit_transform(df[['tenure']])
    monthly = scaler.fit_transform(df[['MonthlyCharges']])
    df['tenure'] = tenure
    df['MonthlyCharges'] = monthly
    
    # elimino le colonne inutili
    df.drop(['customerID','gender','PhoneService','Contract'], axis=1, inplace=True)
    return df
