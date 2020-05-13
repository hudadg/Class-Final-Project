import pickle
from pandas import DataFrame, get_dummies

model = pickle.load(open('finalized_model.sav','rb'))


def prediction(data):
    df = DataFrame(data,index=[0])

    hasil = model.predict(df)
    if hasil == 1 :
        return 'Default'
    else :
        return 'Not Default'