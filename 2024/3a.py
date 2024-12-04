import re

with open("data/input_3.txt", "r") as f:
	data = f.read()

sequences = re.findall('mul\((-?\d+),(-?\d+)\)',data)

print("SUM: ", sum(int(x)*int(y) for x,y in sequences))
