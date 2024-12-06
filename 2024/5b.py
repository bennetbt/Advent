
rules = []
pages = []
with open('data/input_5.txt','r') as f:
	for line in f:
		line = line.strip()
		if '|' in line:
			rules.append(tuple(map(int, line.split('|'))))
		if ',' in line:
			pages.append(list(map(int,line.split(','))))

counter = 0
right_pages = []
wrong_pages = []
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
		counter += 1
		right_pages.append(page)
	else:
		wrong_pages.append(page)
		next

changed = True
while changed:
	changed = False
	for page in wrong_pages:
		for rule in rules:
			if rule[0] in page and rule[1] in page:
				if page.index(rule[0]) > page.index(rule[1]):
					page[page.index(rule[0])],page[page.index(rule[1])] = page[page.index(rule[1])],page[page.index(rule[0])]
					changed = True

middle_sum = 0
for page in wrong_pages:
	middle_sum += page[len(page)//2]
	
print("Middle Sum",middle_sum)
