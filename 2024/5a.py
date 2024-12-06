
rules = []
pages = []
with open('data/input_5.txt','r') as f:
	for line in f:
		line = line.replace('\n','')
		if '|' in line:
			rules.append(tuple(map(int, line.split('|'))))
		if ',' in line:
			pages.append(list(map(int,line.split(','))))

right_pages = []
for page in pages:
	rule_met = True
	for rule in rules:
		if rule[0] in page and rule[1] in page:
			if page.index(rule[0]) < page.index(rule[1]):
				rule_met = True
			else:
				rule_met = False
				break
	if rule_met:
		right_pages.append(page)
	else:
		next

middle_sum = 0
for page in right_pages:
	middle_sum += page[len(page)//2]
	
print("Middle Sum",middle_sum)
