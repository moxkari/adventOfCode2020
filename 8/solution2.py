def test_run(instructions, max_iter=1000):
	executed_indices = set()
	accumulator = 0
	current_index = 0
	iters = 0
	while iters < max_iter:
		iters += 1
		if current_index in executed_indices:
			return -1
		executed_indices.add(current_index)
		if current_index == len(instructions):
			return accumulator
		line = instructions[current_index]
		op, arg = line.strip().split(' ')
		if op == 'nop':
			current_index += 1
		elif op == 'acc':
			current_index += 1
			accumulator += int(arg)
		else: # 'jmp'
			current_index += int(arg)
	return -1


if __name__ == '__main__':
	with open("input.txt", "r") as file:
		lines = file.readlines()
		for i in range(len(lines)):
			line = lines[i]
			op, arg = line.strip().split(' ')
			if op == 'nop' or op == 'jmp':
				fixed_lines = list(lines)
				if op == 'nop':
					op = 'jmp'
				else:
					op = 'nop'
				fixed_lines[i] = op + ' ' + arg
				test_result = test_run(fixed_lines)
				if test_result > 0:
					print(test_result)
					break



