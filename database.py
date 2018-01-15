import pickle
dct={'123':'Anant','456':'jack','789':'ovo'}

with open('dct.pickle','wb') as f:
    pickle.dump(dct,f)
