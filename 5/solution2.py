import math

def b_search(steps, low_char, high_char):
	lower_b = 0
	upper_b = pow(2, len(steps))-1
	for step in steps:
		midpoint = (upper_b-lower_b)/2
		if step == low_char:
			# reduce upper bound by half
			upper_b = math.floor(upper_b - midpoint)
#			print('ub ->' + str(upper_b))
		else:
			lower_b = math.ceil(lower_b + midpoint)
#			print('lb ->' + str(lower_b))
#	print(str(lower_b) + ", " + str(upper_b))
	return lower_b



if __name__ == '__main__':
	with open("input.txt", "r") as file:		
		lines = [l.strip() for l in file.readlines()]
		n = 128
		m = 8
		ids = [[0] * m for i in range(n)]
		for line in lines:
			row = b_search(line[0:7], 'F', 'B')
			col = b_search(line[7:], 'L', 'R')
			ids[row][col] = 1
		empty_front = True
		solution = -1
		for i in range(n):
			if solution > 0:
				break
			for j in range(m):
				if ids[i][j] == 1:
					empty_front = False
				if ids[i][j] == 0 and not empty_front:
					solution = i*8 + j
					break
		print(solution)