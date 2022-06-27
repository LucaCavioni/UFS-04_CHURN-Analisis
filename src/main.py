from data.carica_dati import get_data
from sklearn.model_selection import train_test_split
import sys
sys.path.append('src')
from model.predict import use_model
from model.train import train_model



df = get_data()

X = df.iloc[:, :-1]
Y = df.iloc[:,  -1]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.20,random_state=42)

model = train_model(X_train, Y_train)
pred_pass = use_model(X_test, model)
pred_load = use_model(X_test)

