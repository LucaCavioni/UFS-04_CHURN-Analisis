from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
import sys
sys.path.append('src')
from data.carica_dati import get_data
import pickle

def train_model(X_train, Y_train):
    '''train del modello attraverso le features di train_model
    
    :param df or arraylike type X_train: features di input
    :param series or arraylike Y_train: target
    :return RandomForestClassifier: modello di classificazione 
    '''    
    model = RandomForestClassifier(max_depth= 15, n_estimators = 300)
    model.fit(X_train,Y_train)

    pickle.dump(model, open('model/model.sav', 'wb'))

    return model

def tuning(X_train, Y_train, **kargs):
    # TODO fcontrollo sulle chiavi del kargs
    model = RandomForestClassifier()

    clf = GridSearchCV(model, param_grid=kargs, n_jobs=-1, cv=5)
    clf.fit(X_train, Y_train)
    return clf
