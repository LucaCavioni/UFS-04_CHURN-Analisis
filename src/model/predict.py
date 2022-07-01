import pickle
import sys
sys.path.append('src')

def use_model(X_test, m = None):
    '''predice i valori target per le features passate in input

    :param df or arraylike X_test: features su cui fare le previsioni
    :param estimator m: modello creato in precedenza, defaults to None
    :return arraylike: predizioni
    '''    
    try:
        model = pickle.load(open('model/model.sav', 'rb'))
        return model.predict(X_test)
    except Exception as e:
        if m:
            return m.predict(X_test)
        else:
            print(e)
            
    
