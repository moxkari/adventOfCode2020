import argparse

def toboggan_check(step_x, step_y):
	x = 0
	y = 0
	with open("input.txt", "r") as file:
		lines = [l.strip() for l in file.readlines()]
		count_tree = 0
		line_len = len(lines[0])
		while y < len(lines):			
			if lines[y][x % line_len] == '#':
				count_tree += 1
			# else:
			# 	raise Exception("y=" + str(y) + ", x=" + str(x) + ", ->" + str(lines[y][x % line_len]))
			x += int(step_x)
			y += int(step_y)
		print(str(count_tree))
		return count_tree

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-x') #, '--output')
    # parser.add_argument('-y') #, dest='verbose', action='store_true')
    # args = parser.parse_args()
    # toboggan_check(args.x, args.y)
    print(str(toboggan_check(1,1)*toboggan_check(3,1)*toboggan_check(5,1)*toboggan_check(7,1)*toboggan_check(1,2)))



