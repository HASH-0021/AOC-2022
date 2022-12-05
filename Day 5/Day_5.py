def create_structure_and_instructions():
	for i in range(len(my_list)):
		if my_list[i][:3] == " 1 ":
			break
		level = my_list[i].strip("\n")
		if not i:
			structure = [[] for i in range((len(level)+1)//4)]
		for j in range(1,len(level),4):
			if level[j] != ' ':
				structure[j//4].insert(0,level[j])
	i += 2
	instructions = []
	for j in range(i,len(my_list)):
		step = my_list[j].strip("\n").split(' ')
		no_of_crates = int(step[1])
		start = int(step[3])-1
		end = int(step[5])-1
		instructions.append((no_of_crates,start,end))
	return structure,instructions

def part_1():
	structure,instructions = create_structure_and_instructions()
	for no_of_crates,start,end in instructions:
		for _ in range(no_of_crates):
			structure[end].append(structure[start].pop())
	return ''.join(stack[-1] for stack in structure if stack)

def part_2():
	structure,instructions = create_structure_and_instructions()
	for no_of_crates,start,end in instructions:
		structure[end].extend(structure[start][-no_of_crates:])
		del structure[start][-no_of_crates:]
	return ''.join(stack[-1] for stack in structure if stack)


with open("Structure and Instructions.txt",'r') as my_file:
	my_list = my_file.readlines()

print(f"Crates on top of each stack after rearrangement combines into \"{part_1()}\".")
print(f"Crates on top of each stack after rearrangement using \"CrateMover 9001\" combines into \"{part_2()}\".")