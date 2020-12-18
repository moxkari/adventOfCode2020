from copy import deepcopy

def evolve(A, n, m, C):
	B = deepcopy(A)
	D = deepcopy(C)
	for i in range(n):  	# row
		for j in range(m):	# col
			state = A[i][j]
			if state == '.':
				continue
			else:
				if state == 'L' and C[i][j] == 0:
					B[i][j] = '#'
					for x in range(min(i-1, 0), max(i+1, n-1)):
						for y in range(min(j-1, 0), max(j+1, m)):
							if x != i and y != j:
								D[i][j] += 1
				elif state == '#' and C[i][j] >= 4:
					B[i][j] = 'L'
					for x in range(min(i-1, 0), max(i+1, n-1)):
						for y in range(min(j-1, 0), max(j+1, m)):
							if x != i and y != j:
								D[i][j] -= 1
	return B, D


def generate_init_count(A, n, m):
	C = [[-1 for mm in range(m)] for nn in range(n)]
	for i in range(n):
		for j in range(m):
			state = A[i][j]
			if state == '.':
				C[i][j] = 0
			else:
				adj_seats = 0				
				for x in range(min(i-1, 0), max(i+1, n-1)):
					for y in range(min(j-1, 0), max(j+1, m)):
						if x != i and y != j and A[x][y] == '#':
							adj_seats += 1
				C[i][j] = adj_seats
	return C


with open("input.txt", "r") as file:
	lines = file.readlines()
	matrix = []
	for line in lines:
		matrix.append([c for c in line.strip()])
	n = len(matrix)		# 93
	m = len(matrix[0])	# 94
	counts = generate_init_count(matrix, n, m)
	gen_count = 0
	while True:
		print('round', gen_count)
		next_gen, next_counts = evolve(matrix, n, m, counts)
		gen_count += 1
		if next_gen == matrix:
			final_count = 0
			for row in matrix:
				for c in row:
					if c == '#':
						final_count += 1
			print('final_count', final_count)
			break
		matrix = next_gen
		counts = next_counts
