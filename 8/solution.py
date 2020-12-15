with open("input.txt", "r") as file:
	lines = file.readlines()
	executed_indices = set()
	accumulator = 0
	current_index = 0
	while True:
		print('cur=' + str(current_index) + ', ' + lines[current_index])
		if current_index in executed_indices:
			print(accumulator)
			break
		executed_indices.add(current_index)
		line = lines[current_index]
		op, arg = line.strip().split(' ')
		if op == 'nop':
			current_index += 1
		elif op == 'acc':
			current_index += 1
			accumulator += int(arg)
		else: # 'jmp'
			current_index += int(arg)