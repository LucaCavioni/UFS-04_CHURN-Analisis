import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def pulisci_df(df):
    # fattorizzo le colonne object
    ls_colonne = ['SeniorCitizen', 'Partner', 'Dependents', 'MultipleLines', 'InternetService', 'OnlineSecurity',
                  'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'PaperlessBilling', 'PaymentMethod']
    df = pd.get_dummies(df, ls_colonne, drop_first=True)
    
    # scaler delle colonne continue
    scaler = MinMaxScaler()
    tenure = scaler.fit_transform(df[['tenure']])
    monthly = scaler.fit_transform(df[['MonthlyCharges']])
    df['tenure'] = tenure
    df['MonthlyCharges'] = monthly
    return df
