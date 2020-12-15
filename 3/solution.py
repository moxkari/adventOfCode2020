with open("input.txt", "r") as file:
	lines = [l.strip() for l in file.readlines()]
	x = 0
	y = 0
	count_tree = 0
	count_open = 0
	line_len = len(lines[0])
	print('line_len=' + str(line_len))
	while y < len(lines):
#		print('y='+str(y)+', x='+str(x)+',  xx=' + str(x % line_len))
		if lines[y][x % line_len] == '#':
			count_tree += 1
		elif lines[y][x % line_len] == '.':
			count_open += 1
		else:
			raise Exception("y=" + str(y) + ", x=" + str(x) + ", ->" + str(lines[y][x % line_len]))
		x += 3
		y += 1
	print(str(count_tree))



