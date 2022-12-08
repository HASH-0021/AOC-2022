def part_1():
	visible_trees = 2*(row_len-1) + 2*(col_len-1)
	for i in range(1,row_len-1):
		for j in range(1,col_len-1):
			if max(row[j] for row in my_list[:i]) < my_list[i][j]:
				visible_trees += 1
				continue
			if max(my_list[i][j+1:]) < my_list[i][j]:
				visible_trees += 1
				continue
			if max(row[j] for row in my_list[i+1:]) < my_list[i][j]:
				visible_trees += 1
				continue
			if max(my_list[i][:j]) < my_list[i][j]:
				visible_trees += 1
				continue
	return visible_trees

def part_2():
	scenic_score = 0
	for i in range(1,row_len-1):
		for j in range(1,col_len-1):
			score = 1
			for r in range(i-1,-1,-1):
				if my_list[r][j] >= my_list[i][j]:
					break
			score *= i-r
			for c in range(j+1,col_len):
				if my_list[i][c] >= my_list[i][j]:
					break
			score *= c-j
			for r in range(i+1,row_len):
				if my_list[r][j] >= my_list[i][j]:
					break
			score *= r-i
			for c in range(j-1,-1,-1):
				if my_list[i][c] >= my_list[i][j]:
					break
			score *= j-c
			scenic_score = max(score,scenic_score)
	return scenic_score


with open("Tree Height Map.txt","r") as my_file:
	my_list = [[int(n) for n in row.strip('\n')] for row in my_file.readlines()]

row_len,col_len = len(my_list),len(my_list[0])
print(f"Total of {part_1()} trees are visible from outside the grid.")
print(f"Highest scenic score possible in the map is {part_2()}.")