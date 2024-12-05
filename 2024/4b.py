import numpy as np

with open('data/input_4.txt','r') as f:
        data = [list(line) for line in f.read().split()]

data = np.array(data)
rows,cols = data.shape
word = "MAS"

directions = [
	(1,1),	# Go Down-Right
	(-1,-1),# Go Up-Left
	(1,-1), # Go Down-Left
	(-1,1)	# Go Up-Right
]

def check_x(x,y):
	matches = [
	            [(x-1,y-1,'M'),(x,y,'A'),(x+1,y+1,'S'),(x-1,y+1,'M'),(x+1,y-1,'S')],
	            [(x-1,y-1,'M'),(x,y,'A'),(x+1,y+1,'S'),(x-1,y+1,'S'),(x+1,y-1,'M')],
	            [(x-1,y-1,'S'),(x,y,'A'),(x+1,y+1,'M'),(x-1,y+1,'S'),(x+1,y-1,'M')],
	            [(x-1,y-1,'S'),(x,y,'A'),(x+1,y+1,'M'),(x-1,y+1,'M'),(x+1,y-1,'S')]
	          ]
	for pattern in matches:
		if all(0 <= nx < rows and 0 <= ny < cols and data[nx][ny] == char for nx, ny, char in pattern):
			return True
	
	return False


def find_christmases(As):
	counter = 0
	for l in As:
		if(check_x(l[0],l[1])):
			counter += 1

	return(counter)

#--- Locate all X's
As = [index for index,item in np.ndenumerate(data) if item == 'A']

print(find_christmases(As))
