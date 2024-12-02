import pandas as pd

data = pd.read_csv('data/input_1.txt',header=None,sep='\s+',names=['left','right'])

data['left'] = sorted(data['left'])
data['right'] = sorted(data['right'])

scores = [i*list(data['right']).count(i) for i in data['left']]

print(sum(scores))
