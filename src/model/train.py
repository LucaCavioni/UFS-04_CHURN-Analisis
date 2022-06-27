from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import sys
sys.path.append('src')
from data.carica_dati import get_data
import pickle

def train_model(X_train, Y_train):

    # X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.20,random_state=42)

    model = RandomForestClassifier(max_depth= 15, n_estimators = 300)
    model.fit(X_train,Y_train)

    pickle.dump(model, open('model/model.sav', 'wb'))

    return model
