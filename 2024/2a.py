import io

lines = []

def is_monotonic(levels):
	non_decr = [i<=j for i,j in zip(levels,levels[1:])]
	non_incr = [i>=j for i,j in zip(levels,levels[1:])]
	return all(non_decr) or all(non_incr)

def valid_diffs(levels):
	return all([abs(i-j) >= 1 and abs(i-j) <= 3 for i,j in zip(levels,levels[1:])])

with io.open('data/input_2.txt', mode='r') as f:
	for line in f:
		lines.append([int(x) for x in line.split()])

counter = 0
for row in lines:
	if (is_monotonic(row) and valid_diffs(row)):
		counter += 1

print("Total: ",counter)
