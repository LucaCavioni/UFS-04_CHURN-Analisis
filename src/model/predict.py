import pickle
import sys
sys.path.append('src')

def use_model(X_test, m = None):
    try:
        model = pickle.load(open('model/model.sav', 'rb'))
        return model.predict(X_test)
    except Exception as e:
        if m:
            return m.predict(X_test)
        else:
            print(e)
            
    
