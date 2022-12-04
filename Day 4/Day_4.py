def part_1():
	count = 0
	for pair in section_pairs:
		pair = pair.strip('\n').split(',')
		s1,s2 = [[int(x) for x in section.split('-')] for section in pair]
		if (s1[0]<=s2[0] and s1[1]>=s2[1]) or (s2[0]<=s1[0] and s2[1]>=s1[1]):
			count += 1
	return count

def part_2():
	count = 0
	for pair in section_pairs:
		pair = pair.strip('\n').split(',')
		s1,s2 = [[int(x) for x in section.split('-')] for section in pair]
		if s1[0]<=s2[0]<=s1[1] or s2[0]<=s1[0]<=s2[1]:
			count += 1
	return count

with open("Section Assignment Pairs.txt",'r') as my_file:
	section_pairs = my_file.readlines()

print(f"One section range fully contains the other in {part_1()} pairs.")
print(f"Section ranges overlap in {part_2()} pairs.")