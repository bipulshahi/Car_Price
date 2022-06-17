import pickle
import json
import numpy as np

_data_columns = None
_model = None

def load_artifacts():
    global _data_columns
    global _model
    
    print('loading artifacts....')

    with open('./columns.json','r') as f:
        _data_columns = json.load(f)['features']

    with open('./car_price.pickle','rb') as f:
        _model = pickle.load(f)

    print('Artifacts loaded suceessfully')

def predict_car_prices(year,kms,mlg,engine,power,seats,location,
                       fuelType,transType,ownerType,carName):

    input = np.zeros(len(_data_columns))

    input[0] = year
    input[1] = kms
    input[2] = mlg
    input[3] = engine
    input[4] = power
    input[5] = seats

    loc = _data_columns.index(location.lower())
    ftype = _data_columns.index(fuelType.lower())
    ttype = _data_columns.index(transType.lower())
    otype = _data_columns.index(ownerType.lower())
    cname = _data_columns.index(carName.lower())

    input[loc] = 1
    input[ftype] = 1
    input[ttype] = 1
    input[otype] = 1
    input[cname] = 1

    return _model.predict([input])[0][0]

def get_feature_names():
    return _data_columns


load_artifacts()
#get_feature_names()
print(predict_car_prices(10,20000,20,990,56,5,'Mumbai','Petrol','Manual',
                         'First','honda jazz'))
