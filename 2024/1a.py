import pandas as pd

data = pd.read_csv('data/input_1.txt',header=None,sep='\s+')

left = data[0].to_list()
right = data[1].to_list()

left.sort()
right.sort()
diff = [abs(i-j) for i,j in list(zip(left,right))]

print(sum(diff))
