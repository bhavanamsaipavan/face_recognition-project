import pandas as pd

data = pd.read_csv('referance.csv')

req_dat = data.dict()

for i in range(1, len(data['Name'])):
    