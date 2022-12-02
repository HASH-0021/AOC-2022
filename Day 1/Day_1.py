with open("Calories List.txt",'r') as my_file:
	calories_list = my_file.readlines()

def part_1():
	max_calories = food = 0
	for item in calories_list:
		calories = item.strip('\n')
		if not calories:
			max_calories = max(max_calories,food)
			food = 0
		else:
			food += int(calories)
	return max(max_calories,food)

def part_2():
	my_list,food = [],0
	for item in calories_list:
		calories = item.strip('\n')
		if not calories:
			my_list.append(food)
			if len(my_list) > 3:
				my_list.sort(reverse=True)
				my_list.pop()
			food = 0
		else:
			food += int(calories)
	my_list.append(food)
	if len(my_list) > 3:
		my_list.sort(reverse=True)
		my_list.pop()
	return sum(my_list)


print(f"Elf carrying most calories has {part_1()} calories.")
print(f"Top three elves carrying most calories have {part_2()} calories in total.")