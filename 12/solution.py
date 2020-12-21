import re

DIR_OPS = ['E', 'S', 'W', 'N']

def turn(turn_direction, degrees, index):
	while degrees > 0:
		degrees -= 90
		if turn_direction == 'R':
			index = (index + 1) % len(DIR_OPS)
		else:
			index = (index - 1) % len(DIR_OPS)
	return index


def sail(direction, arg, x, y):
	if direction == 'E':
		return x+arg, y
	elif direction == 'W':
		return x-arg, y
	elif direction == 'N':
		return x, y-arg
	else:
		return x, y+arg


with open("input.txt", "r") as file:
	lines = file.readlines()
	current_dir_idx = 0		# first in DIR_OPS = 'E'
	x_coord = 0
	y_coord = 0
	for line in lines:
		line = line.strip()
		op = line[0]
		arg = int(line[1:])
		if op in DIR_OPS:
			x_coord, y_coord = sail(op, arg, x_coord, y_coord)
		elif op == 'F':
			x_coord, y_coord = sail(DIR_OPS[current_dir_idx], arg, x_coord, y_coord)
		else:
			current_dir_idx = turn(op, arg, current_dir_idx)
	print('Manhattan dist:', abs(x_coord)+abs(y_coord))