import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder
import pickle


def pulisci_df(df: pd.DataFrame):
    '''ritorna un dataframe pulito utilizzando, trainando e salvando i modelli per il preprocessing dei dati

    :param pd.DataFrame df: df da pulire
    :return df
    '''    
    # elimino le colonne inutili
    df.drop(['customerID','gender','PhoneService','Contract'], axis=1, inplace=True)
    
    # elimino i dati null e definisco il tipo della colonna
    df = df.drop(df[df['TotalCharges'] == ' '].index)
    df.TotalCharges = df['TotalCharges'].astype(float)
    
    # utilizzo la ordinal encoder per le colonne object
    oe = OrdinalEncoder()
    print(df.select_dtypes(include='object').shape)
    df[df.select_dtypes(include='object').columns] = oe.fit_transform(df.select_dtypes(include='object'))
    # salvo il modello
    pickle.dump(oe, open('model/oe_model.sav', 'wb'))
    
    # scaler delle colonne continue
    scaler = MinMaxScaler()
    tenure = scaler.fit_transform(df[['tenure']])
    monthly = scaler.fit_transform(df[['MonthlyCharges']])
    df['tenure'] = tenure
    df['MonthlyCharges'] = monthly
    pickle.dump(scaler, open('model/scaler_model.sav', 'wb'))
    
    return df

def preprocessing(df: pd.DataFrame):
    '''ritorna un dataframe pulito utilizzando i modelli salvati in precedenza per il preprocessing dei dati

    :param pd.DataFrame df: df da pulire
    :return df
    '''    
    # ciclo che elimina se trova le colonne inutili
    for e in df.copy().columns:
        if e in ['customerID','gender','PhoneService','Contract']:
            df.drop(columns=e, inplace=True)
    print(df)
    # elimino i dati null e definisco il tipo della colonna
    if 'TotalCharges' in df.columns:
        df = df.drop(df[df['TotalCharges'] == ' '].index)
        df.TotalCharges = df['TotalCharges'].astype(float)
    try:
        # carico e utilizzo l'OrdinalEncoder
        oe      = pickle.load(open('model/oe_model.sav', 'rb'))       
        df[df.select_dtypes(include='object').columns] = oe.transform(df.select_dtypes(include='object'))
        # carico e utilizzo il MinMaxScaler 
        scaler  = pickle.load(open('model/scaler_model.sav', 'rb'))
        tenure  = scaler.transform(df[['tenure']])
        monthly = scaler.transform(df[['MonthlyCharges']])
        df['tenure'] = tenure
        df['MonthlyCharges'] = monthly
    except Exception as e:
        print(e)
    
    return df