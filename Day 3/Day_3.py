def part_1():
	total = 0
	for each_rucksack in all_items:
		items = each_rucksack.strip('\n')
		mid = len(items)//2
		for x in items[:mid]:
			if x in items[mid:]:
				if 97 <= ord(x) <= 122:
					total += ord(x)-96
				if 65 <= ord(x) <= 90:
					total += ord(x)-38
				break
	return total

def part_2():
	total = 0
	for idx in range(0,len(all_items),3):
		items_1 = set(all_items[idx].strip('\n'))
		items_2 = set(all_items[idx+1].strip('\n'))
		items_3 = set(all_items[idx+2].strip('\n'))
		for x in items_1:
			if x in items_2 and x in items_3:
				if 97 <= ord(x) <= 122:
					total += ord(x)-96
				if 65 <= ord(x) <= 90:
					total += ord(x)-38
				break
	return total

with open("Rucksacks Items.txt",'r') as my_file:
	all_items = my_file.readlines()

print(f"Sum of priorities of failed item types is {part_1()}.")
print(f"Sum of priorities of each group's badge item type is {part_2()}.")