def find_start_points():
	start_points = []
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 'S':
				curr_pos = (i,j)
			if grid[i][j] == 'a':
				start_points.append((i,j))
	return [curr_pos]+start_points

def part_1():
	queue = [(*start_points[0],0)]
	visited = set()
	while queue:
		r,c,steps = queue.pop(0)
		if (r,c) in visited:
			continue
		visited.add((r,c))
		height = 'a' if grid[r][c] == 'S' else grid[r][c]
		next_heights = []
		if r-1 >= 0:
			next_heights.append((r-1,c))
		if c+1 < len(grid[0]):
			next_heights.append((r,c+1))
		if r+1 < len(grid):
			next_heights.append((r+1,c))
		if c-1 >= 0:
			next_heights.append((r,c-1))
		for x,y in next_heights:
			next_height = grid[x][y]
			if next_height == 'E' and ord('z')-ord(height) <= 1:
				return steps+1
			if next_height != 'E' and ord(next_height)-ord(height) <= 1:
				queue.append((x,y,steps+1))
	return -1

def part_2():
	min_steps = float("inf")
	for start_point in start_points:
		queue = [(*start_point,0)]
		visited = set()
		goal_reached = False
		while queue:
			r,c,steps = queue.pop(0)
			if (r,c) in visited:
				continue
			visited.add((r,c))
			height = 'a' if grid[r][c] == 'S' else grid[r][c]
			next_heights = []
			if r-1 >= 0:
				next_heights.append((r-1,c))
			if c+1 < len(grid[0]):
				next_heights.append((r,c+1))
			if r+1 < len(grid):
				next_heights.append((r+1,c))
			if c-1 >= 0:
				next_heights.append((r,c-1))
			for x,y in next_heights:
				next_height = 'a' if grid[x][y] == 'S' else grid[x][y]
				if next_height == 'E' and ord('z')-ord(height) <= 1:
					min_steps = min(min_steps,steps+1)
					goal_reached = True
					break
				if next_height != 'E' and ord(next_height)-ord(height) <= 1:
					queue.append((x,y,steps+1))
			if goal_reached:
				break
	return min_steps if min_steps != float("inf") else -1

with open("Height Map.txt",'r') as my_file:
	grid = [list(row.strip('\n')) for row in my_file.readlines()]

start_points = find_start_points()
print(f"Fewest possible steps to reach the location with best signal from current location is {part_1()}.")
print(f"Fewest possible steps to reach the location with best signal from any lowest elevation is {part_2()}.")