def part_1(monkeys):
	inspect_count = [0]*len(monkeys)
	for _ in range(20):
		for idx,monkey in enumerate(monkeys):
			inspect_count[idx] += len(monkey[0])
			while monkey[0]:
				worry_level = monkey[0].pop(0)
				a,op,b = monkey[1]
				if op == '*':
					worry_level *= int(b) if b.isnumeric() else worry_level
				elif op == '+':
					worry_level += int(b) if b.isnumeric() else worry_level
				worry_level //= 3
				if worry_level%monkey[2]:
					monkeys[monkey[3][1]][0].append(worry_level)
				else:
					monkeys[monkey[3][0]][0].append(worry_level)
	active_inspections = sorted(inspect_count)[-2:]
	return active_inspections[0]*active_inspections[1]

def part_2(monkeys):
	inspect_count = [0]*len(monkeys)
	new_relief = 1
	for monkey in monkeys:
		new_relief *= monkey[2]
	for _ in range(10000):
		for idx,monkey in enumerate(monkeys):
			inspect_count[idx] += len(monkey[0])
			while monkey[0]:
				worry_level = monkey[0].pop(0)
				a,op,b = monkey[1]
				if op == '*':
					worry_level *= int(b) if b.isnumeric() else worry_level
				elif op == '+':
					worry_level += int(b) if b.isnumeric() else worry_level
				worry_level %= new_relief
				if worry_level%monkey[2]:
					monkeys[monkey[3][1]][0].append(worry_level)
				else:
					monkeys[monkey[3][0]][0].append(worry_level)
	active_inspections = sorted(inspect_count)[-2:]
	return active_inspections[0]*active_inspections[1]

with open("Notes.txt",'r') as my_file:
	notes = my_file.readlines()

monkeys = []
for note in notes:
	if note == '\n':
		continue
	note = note.strip('\n').split(' ')
	note = [n for n in note if n]
	if note[0][0] == 'M':
		monkeys.append([])
	if note[0][0] == 'S':
		monkeys[-1].append([int(item.split(',')[0]) for item in note[2:]])
	if note[0][0] == 'O':
		monkeys[-1].append(note[3:])
	if note[0][0] == 'T':
		monkeys[-1].append(int(note[-1]))
		monkeys[-1].append([])
	if note[0][0] == 'I':
		monkeys[-1][-1].append(int(note[-1]))

print(f"Level of monkey business after 20 rounds is {part_1([[monkey[0][:]]+monkey[1:] for monkey in monkeys])}.")
print(f"Level of monkey business after 10000 rounds with new relief is {part_2([[monkey[0][:]]+monkey[1:] for monkey in monkeys])}.")