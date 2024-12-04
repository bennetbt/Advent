import re

with open("data/input_3.txt", "r") as f:
	data = f.read()

commands = [('do',l.start(0),l.end(0)) for l in re.finditer('do\(\)',data)] + [('dont',l.start(0),l.end(0)) for l in re.finditer("don't\(\)",data)] + [('mul',l.start(0),l.end(0)) for l in re.finditer("mul\((-?\d+),(-?\d+)\)",data)]
commands = sorted(commands, key=lambda x:x[1])

do = True
result = 0
for command in commands:
	if command[0] == 'do':
		do = True
	elif command[0] == 'dont':
		do = False

	if command[0] == 'mul' and do:
		amt = tuple(int(i) if i.isdigit() else i for i in data[command[1]+4:command[2]-1].split(','))
		result += amt[0]*amt[1]

print("Sum:",result)
