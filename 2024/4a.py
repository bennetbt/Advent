import numpy as np

with open('data/input_4.txt','r') as f:
        data = [list(line) for line in f.read().split()]

data = np.array(data)
rows,cols = data.shape
word = "XMAS"

directions = [
	(0,1), 	# Go right
	(0,-1), # Go left
	(1,0),  # Go down
	(-1,0),	# Go Up
	(1,1),	# Go Down-Right
	(-1,-1),# Go Up-Left
	(1,-1), # Go Down-Left
	(-1,1)	# Go Up-Right
]

def check_direction(r, c, dr, dc):
	for i in range(4):
		nr, nc = r + dr * i, c + dc * i
		if not (0 <= nr < rows and 0 <= nc < cols) or data[nr][nc] != word[i]:
			return False
	return True


def find_christmases(xs):
	counter = 0
	for l in xs:
		for d in directions:
			if(check_direction(l[0],l[1],d[0],d[1])):
				counter += 1

	return(counter)

#--- Locate all X's
Xs = [index for index,item in np.ndenumerate(data) if item == 'X']

print(find_christmases(Xs))
