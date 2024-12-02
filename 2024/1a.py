import pandas as pd

data = pd.read_csv('data/input_1.txt',header=None,sep='\s+',names=['left','right'])

data['left'] = sorted(data['left'])
data['right'] = sorted(data['right'])

diff_sum = (data['left'] - data['right']).abs().sum()

print(diff_sum)
