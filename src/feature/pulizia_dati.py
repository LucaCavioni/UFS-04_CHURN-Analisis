import pandas as pd


def pulisci_df(df):
    # elimino i dati null e definisco il tipo della colonna
    df = df.drop(df[df['TotalCharges'] == ' '].index)
    df.TotalCharges = df['TotalCharges'].astype(float)

    # fattorizzo le colonne object
    df = df.select_dtypes(include='object')
    df = df.apply(lambda x: x.factorize()[0])
    return df