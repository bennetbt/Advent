import io
import copy

lines = []

def is_monotonic(levels):
	non_decr = [i<=j for i,j in zip(levels,levels[1:])]
	non_incr = [i>=j for i,j in zip(levels,levels[1:])]
	return all(non_decr) or all(non_incr)

def valid_diffs(levels):
	return all([abs(i-j) >= 1 and abs(i-j) <= 3 for i,j in zip(levels,levels[1:])])

def try_dampener(levels):
	l = copy.deepcopy(levels)
	for i in range(0,len(levels)):
		del l[i]
		if (is_monotonic(l) and valid_diffs(l)):
			return True
		l = copy.deepcopy(levels)
	return False

with io.open('data/input_2_test.txt', mode='r') as f:
	for line in f:
		lines.append([int(x) for x in line.split()])

counter = 0
for row in lines:
	if (is_monotonic(row) and valid_diffs(row)):
		counter += 1
	elif (try_dampener(row)):
		counter += 1

print("Total: ",counter)
