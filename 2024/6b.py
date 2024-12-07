import numpy as np
from copy import deepcopy

DIRECTIONS = { '^':(-1,0),'>':(0,1),'v':(1,0),'<':(0,-1) }
CHARACTERS = { '^':'X','>':'X','v':'X','<':'X' }
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
		return map,ptr,position,True
	elif (map[x][y]  == '.'):
		map[x][y] = ptr
		map[position[0]][position[1]] = CHARACTERS[ptr]
		return map,ptr,(x,y),False
	elif (map[x][y] in ['|','-','X']):
		map[x][y] = ptr
		map[position[0]][position[1]] = CHARACTERS[ptr]
		return map,ptr,(x,y),False
	elif (map[x][y] == '#'):
		idx = POINTERS.index(ptr)+1
		if (idx == 4):
			ptr = POINTERS[0]
		else:
			ptr = POINTERS[idx]

		return map,ptr,position,False
	else:
		return map,ptr,position,False


def simulate(field, obstruction=None):
	field = deepcopy(field)
	if obstruction:
		field[obstruction[0]][obstruction[1]] = '#'

	guard = find_guard(field)

	pointer, position = guard
	visited_states = set()
	is_finished = False

	while not is_finished:
		state = (pointer, position)
		if state in visited_states:
			return True  # Loop
		visited_states.add(state)
		field, pointer, position, is_finished = move(field, pointer, position)
    
	return False



def find_obstruction_positions(field):
	obs_positions = []
	for x in range(len(field)):
		for y in range(len(field[0])):
			if field[x][y] == '.':  # Only consider open spaces
				if simulate(field, obstruction=(x, y)):
					obs_positions.append((x, y))
	return obs_positions

field = load_field()

simulate(field,None)

obs_positions = find_obstruction_positions(field)
    
print("Number of valid positions:", len(obs_positions))
