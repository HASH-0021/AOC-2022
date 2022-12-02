def part_1():
	total = 0
	for item in guide:
		opp_move,my_move = item.strip('\n').split(' ')
		my_move = chr(ord(my_move)-23)
		total += shape_score[my_move]
		if (opp_move,my_move) in [('A','B'),('B','C'),('C','A')]:
			total += 6
		if opp_move == my_move:
			total += 3
	return total

def part_2():
	total = 0
	for item in guide:
		opp_move,outcome = item.strip('\n').split(' ')
		score = shape_score[opp_move]
		if outcome == 'X':
			total += score-1 if score-1 else 3
		if outcome == 'Y':
			total += score+3
		if outcome == 'Z':
			total += score+7 if score+1 < 4 else 7
	return total

with open("Strategy Guide.txt",'r') as my_file:
	guide = my_file.readlines()

shape_score = {x : e+1 for e,x in enumerate(('A','B','C'))}
print(f"My total score according to my reason is {part_1()}.")
print(f"My total score according to actual guide is {part_2()}.")