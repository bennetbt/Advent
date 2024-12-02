import io

lines = []

def is_monotonic(levels):
	return all(i<=j for i,j in zip(levels,levels[1:])) or all(i>=j for i,j in zip(levels,levels[1:]))

def valid_diffs(levels):
	return all([abs(i-j) >= 1 and abs(i-j) <= 3 for i,j in zip(levels,levels[1:])])

def try_dampener(levels):
	for i in range(0,len(levels)):
		l = levels[:i] + levels[i+1:]
		if (is_monotonic(l) and valid_diffs(l)):
			return True
	return False

with io.open('data/input_2.txt', mode='r') as f:
	lines = [[int(x) for x in line.split()] for line in f]

counter = sum(1 for row in lines if (is_monotonic(row) and valid_diffs(row)) or try_dampener(row))

print("Total: ",counter)
