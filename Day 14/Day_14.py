def part_1(cave_map):
	start = 500 - min_x
	units = 0
	infinite_flow = False
	while True:
		c,r = start,0
		while True:
			if r+1 == len(cave_map) or c in (0,len(cave_map[0])):
				infinite_flow = True
				break
			if cave_map[r+1][c] == '.':
				c += 0
			elif cave_map[r+1][c-1] == '.':
				c += -1
			elif cave_map[r+1][c+1] == '.':
				c += 1
			else:
				cave_map[r][c] = 'o'
				break
			r += 1
		if infinite_flow:
			break
		units += 1
	return units

def part_2(cave_map):
	cave_map.append(['.' for _ in range(max_x-min_x+1)])
	cave_map.append(['#' for _ in range(max_x-min_x+1)])
	start = 500 - min_x
	units = 0
	while True:
		c = start
		for r in range(len(cave_map)-1):
			if not c:
				for row in cave_map[:-1]:
					row.insert(0,'.')
				cave_map[-1].insert(0,'#')
				start += 1
				c += 1
			elif c == len(cave_map[0])-1:
				for row in cave_map[:-1]:
					row.append('.')
				cave_map[-1].append('#')
			if cave_map[r+1][c] == '.':
				c += 0
			elif cave_map[r+1][c-1] == '.':
				c += -1
			elif cave_map[r+1][c+1] == '.':
				c += 1
			else:
				cave_map[r][c] = 'o'
				break
		units += 1
		if not r:
			break
	return units

with open("Cave Map.txt",'r') as my_file:
	my_list = my_file.readlines()

rock_paths = []
max_x = max_y = 0
min_x = float('inf')
for path in my_list:
	rock_paths.append([])
	for coord in path.strip().split(" -> "):
		rock_paths[-1].append(tuple(int(c) for c in coord.split(",")))
		x,y = rock_paths[-1][-1]
		max_x = max(x,max_x)
		max_y = max(y,max_y)
		min_x = min(x,min_x)

cave_map = [['.' for _ in range(max_x-min_x+1)] for _ in range(max_y+1)]

for path in rock_paths:
	for p in range(len(path)-1):
		cols,rows = zip(path[p],path[p+1])
		min_c,max_c = min(cols),max(cols)
		min_r,max_r = min(rows),max(rows)
		if min_c == max_c:
			for i in range(min_r,max_r+1):
				cave_map[i][min_c-min_x] = "#"
		elif min_r == max_r:
			for j in range(min_c,max_c+1):
				cave_map[min_r][j-min_x] = "#"

print(f"{part_1([row[:] for row in cave_map])} units of sand come to rest before sand starts flowing into the abyss below.")
print(f"{part_2([row[:] for row in cave_map])} units of sand come to rest until the source of the sand becomes blocked.")