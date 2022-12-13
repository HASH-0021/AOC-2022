def create_packet(packet,idx):
	my_packet = []
	i = idx+1
	number = ""
	while i < len(packet):
		if packet[i] == '[':
			data,i = create_packet(packet,i)
			my_packet.append(data)
		elif packet[i] == ']':
			if number:
				my_packet.append(int(number))
			return my_packet,i
		elif packet[i].isdigit():
			number += packet[i]
		elif packet[i] == ',' and number:
			my_packet.append(int(number))
			number = ""
		i += 1

def compare(packet1,packet2):
	idx = 0
	while idx < len(packet1) and idx < len(packet2):
		data1,data2 = packet1[idx],packet2[idx]
		if isinstance(data1,int) and isinstance(data2,int):
			if data1 < data2:
				return "right"
			if data1 > data2:
				return "wrong"
		elif isinstance(data1,int):
			order = compare([data1],data2)
			if order in ("right","wrong"):
				return order
		elif isinstance(data2,int):
			order = compare(data1,[data2])
			if order in ("right","wrong"):
				return order
		else:
			order = compare(data1,data2)
			if order in ("right","wrong"):
				return order
		idx += 1
	if idx < len(packet1):
		return "wrong"
	if idx < len(packet2):
		return "right"
	return "equal"

def part_1():
	total = 0
	for i,pair in enumerate(packets):
		if compare(*pair) == "right":
			total += i+1
	return total

def part_2():
	organized_packets = []
	divider_packets = [[[2]],[[6]]]
	decoder_key = 1
	for i,pair in enumerate(packets+[divider_packets]):
		if not i:
			organized_packets.append(pair[0])
			pair = [pair[1]]
		for p1 in pair:
			idx = len(organized_packets)
			for j,p2 in enumerate(organized_packets):
				if compare(p1,p2) == "right":
					idx = j
					break
			organized_packets.insert(idx,p1)
			if p1 in divider_packets:
				decoder_key *= idx+1
	return decoder_key

with open("Distress Signal.txt",'r') as my_file:
	my_list = my_file.readlines()

packets = []
for i in range(len(my_list)):
	line = my_list[i].strip()
	if i % 3 == 0:
		packets.append([line])
	elif i % 3 == 1:
		packets[-1].append(line)
for pair in packets:
	pair[0] = create_packet(pair[0],0)[0]
	pair[1] = create_packet(pair[1],0)[0]

print(f"Sum of indices of right ordered pairs in distress signal is {part_1()}.")
print(f"Decoder key for the distress signal is {part_2()}.")