import numpy as np

DIRECTIONS = { '^':(-1,0),'>':(0,1),'v':(1,0),'<':(0,-1) }
POINTERS = ['^','>','v','<']


def load_field():
	with open('data/input_6.txt','r') as f:
		return [list(line.strip()) for line in f]


def find_guard(map):
	for pointer in POINTERS:
		for row_idx,row in enumerate(map):
			if pointer in row:
				return pointer, (row_idx, row.index(pointer))
	return None


def move(map,ptr,position):
	displacement = DIRECTIONS[ptr]
	x,y = tuple([sum(x) for x in zip(position,displacement)])
	if (x < 0 or y < 0 or x >= len(map) or y >= len(map[0])):
		return [map,ptr,position,1]
	elif (map[x][y] in ['.','X']):
		map[x][y] = ptr
		map[position[0]][position[1]] = 'X'
		return [map,ptr,(x,y)]
	elif (map[x][y] == '#'):
		idx = POINTERS.index(ptr)+1
		if (idx == 4):
			ptr = POINTERS[0]
		else:
			ptr = POINTERS[idx]

		return [map,ptr,position]
	else:
		return [map,ptr,position]


field = load_field()
guard = find_guard(field)

val = move(field,guard[0],guard[1])
while 1 not in val:
	val = move(val[0],val[1],val[2])

print(sum(x.count('X') for x in val[0])+1)

