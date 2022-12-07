def create_directory(dir_name,idx):
	new_dir,size = {},0
	while idx < len(my_list):
		line = my_list[idx].strip('\n').split(' ')
		if line[0] == "$":
			if line[1] == "cd":
				if line[2] == "..":
					return (new_dir,size),"..",idx
				elif line[2] == "/" and idx:
					return (new_dir,size),"/",idx
				else:
					new_dir[line[2]],back,idx = create_directory(line[2],idx+1)
					size += new_dir[line[2]][1]
					if not back:
						break
					if back == "/" and dir_name != "/":
						return (new_dir,size),"/",idx
		elif line[0] == "dir":
			new_dir[line[1]] = ({},0)
		elif line[0].isnumeric():
			new_dir[line[1]] = int(line[0])
			size += new_dir[line[1]]
		idx += 1
	return (new_dir,size),"",idx

def part_1():
	total = 0
	stack = [filesystem[0]['/']]
	while stack:
		curr_dir,size = stack.pop()
		if size <= 100000:
			total += size
		for name in curr_dir:
			if isinstance(curr_dir[name],tuple):
				stack.append(curr_dir[name])
	return total

def part_2():
	total_space = 70000000
	used_space = filesystem[1]
	unused_space = total_space - used_space
	reqd_space = 30000000
	if unused_space >= reqd_space:
		return 0
	ideal_removal = reqd_space - unused_space
	stack = [filesystem[0]['/']]
	actual_removal = used_space
	while stack:
		curr_dir,size = stack.pop()
		if size >= ideal_removal:
			actual_removal = min(actual_removal,size)
		for name in curr_dir:
			if isinstance(curr_dir[name],tuple):
				stack.append(curr_dir[name])
	return actual_removal

with open("Terminal Output.txt",'r') as my_file:
	my_list = my_file.readlines()

filesystem = create_directory("filesystem",0)[0]
print(f"Sum of total sizes of directories with atmost 100000 total size each is {part_1()}.")
print(f"Total size of smallest directory to be deleted, such that it would free up enough space for update, is {part_2()}.")