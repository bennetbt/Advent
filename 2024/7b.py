import itertools

problems = []
operations = ['*','+','||']

with open('data/input_7.txt','r') as f:
	for line in f:
		problem = []
		line = line.strip()
		line = line.split(":")
		line[1] = tuple(line[1].strip().split(' '))
		problems.append(line)


def evaluate(vals, ops):
	result = int(vals[0])
	for i, op in enumerate(ops):
		if op == '*':
			result *= int(vals[i + 1])
		elif op == '+':
			result += int(vals[i + 1])
		elif op == '||':
			result = int(str(result)+str(vals[i+1]))

	return result


results = []
for problem in problems:

	outcome = []
	result = int(problem[0])
	vals = problem[1]
	
	ops = list(itertools.product(operations, repeat=len(vals)-1))
	
	for o in ops:
		if result != evaluate(vals,o):
			outcome.append(False)
		else:
			outcome.append(True)

	results.append((result,outcome))

#print(results)
print(sum([r[0] for r in results if any(r[1])]))