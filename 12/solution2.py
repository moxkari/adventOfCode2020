import re

def turn(turn_direction, degrees, wp_x, wp_y):
	while degrees > 0:
		degrees -= 90
		if turn_direction == 'R':
			tmp = wp_x
			wp_x = wp_y
			wp_y = -1 * tmp
		else:
			tmp = wp_x
			wp_x = -1*wp_y
			wp_y = tmp
	return wp_x, wp_y


def move_waypoint(direction, dist, wp_x, wp_y):
	if direction == 'E':
		return wp_x+dist, wp_y
	elif direction == 'W':
		return wp_x-dist, wp_y
	elif direction == 'N':
		return wp_x, wp_y+dist
	else:
		return wp_x, wp_y-dist


def sail(x, y, multiplier, wp_x, wp_y):
	return x + multiplier*wp_x, y + multiplier*wp_y


with open("input.txt", "r") as file:
	lines = file.readlines()
	x_coord = 0
	y_coord = 0
	waypoint_x = 10
	waypoint_y = 1
	for line in lines:
		line = line.strip()
		op = line[0]
		arg = int(line[1:])
		if op in DIR_OPS:
			waypoint_x, waypoint_y = move_waypoint(op, arg, waypoint_x, waypoint_y)
#			print('MV WAYPOINT->', waypoint_x, waypoint_y)
		elif op == 'F':
			x_coord, y_coord = sail(x_coord, y_coord, arg, waypoint_x, waypoint_y)
#			print('SAIL',arg,'->', x_coord, y_coord)
		else:
			waypoint_x, waypoint_y = turn(op, arg, waypoint_x, waypoint_y)
#			print('TURN',arg,'->', waypoint_x, waypoint_y)
	print('Manhattan dist:', abs(x_coord)+abs(y_coord))