def part_1():
	for i in range(4,len(buffer)+1):
		if len(set(buffer[i-4:i])) == 4:
			return i

def part_2():
	for i in range(14,len(buffer)+1):
		if len(set(buffer[i-14:i])) == 14:
			return i

with open("Datastream Buffer.txt",'r') as my_file:
	buffer = my_file.read()

print(f"First start-of-packet marker is detected after {part_1()} characters are processed.")
print(f"First start-of-message marker is detected after {part_2()} characters are processed.")