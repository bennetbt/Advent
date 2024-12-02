import pandas as pd

data = pd.read_csv('data/input_1.txt',header=None,sep='\s+')

left = data[0].to_list()
right = data[1].to_list()

left.sort()
right.sort()
scores = [i*right.count(i) for i in left]

print(sum(scores))
