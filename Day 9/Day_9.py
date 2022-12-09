def part_1():
	head_pos = [0,0]
	tail_pos = [0,0]
	tail_visited = {tuple(tail_pos)}
	for direction,distance in movement:
		for _ in range(int(distance)):
			head_pos[0] += steps[direction][0]
			head_pos[1] += steps[direction][1]
			x_dist = abs(head_pos[0]-tail_pos[0])
			y_dist = abs(head_pos[1]-tail_pos[1])
			if x_dist > 1 or y_dist > 1:
				if not x_dist:
					tail_pos[1] += 1 if tail_pos[1] < head_pos[1] else -1
				elif not y_dist:
					tail_pos[0] += 1 if tail_pos[0] < head_pos[0] else -1
				else:
					tail_pos[0] += 1 if tail_pos[0] < head_pos[0] else -1
					tail_pos[1] += 1 if tail_pos[1] < head_pos[1] else -1
				tail_visited.add(tuple(tail_pos))
	return len(tail_visited)

def part_2():
	rope_knots = [[0,0] for _ in range(10)]
	tail_visited = {(0,0)}
	for direction,distance in movement:
		for _ in range(int(distance)):
			rope_knots[0][0] += steps[direction][0]
			rope_knots[0][1] += steps[direction][1]
			for i in range(1,10):
				prev,curr = rope_knots[i-1:i+1]
				x_dist = abs(curr[0]-prev[0])
				y_dist = abs(curr[1]-prev[1])
				if x_dist > 1 or y_dist > 1:
					if not x_dist:
						curr[1] += 1 if curr[1] < prev[1] else -1
					elif not y_dist:
						curr[0] += 1 if curr[0] < prev[0] else -1
					else:
						curr[0] += 1 if curr[0] < prev[0] else -1
						curr[1] += 1 if curr[1] < prev[1] else -1
					if i == 9:
						tail_visited.add(tuple(curr))
				else:
					break
	return len(tail_visited)

with open("Hypothetical series of motions.txt",'r') as my_file:
	movement = [move.strip('\n').split(' ') for move in my_file.readlines()]

steps = {
	"U"	:	[-1,0],
	"R"	:	[0,1],
	"D"	:	[1,0],
	"L"	:	[0,-1]
}

print(f"Tail of the rope with 2 knots visited {part_1()} position(s) atleast once.")
print(f"Tail of the rope with 10 knots visited {part_2()} position(s) atleast once.")