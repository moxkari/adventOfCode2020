from copy import deepcopy

def evolve(A, C, q, n, m):
	D = deepcopy(C)
	qq = set()
	for (i, j) in q:
		state = A[i][j]
		if state == '.':
			continue
		else:
			if state == 'L' and C[i][j] == 0:
				A[i][j] = '#'
				qq.add((i, j))
				for x in range(max(i-1, 0), min(i+2, n)):
					for y in range(max(j-1, 0), min(j+2, m)):
						if not (x==i and y==j):
							D[x][y] += 1
							qq.add((x, y))
			elif state == '#' and C[i][j] >= 4:
				A[i][j] = 'L'
				qq.add((i, j))
				for x in range(max(i-1, 0), min(i+2, n)):
					for y in range(max(j-1, 0), min(j+2, m)):
						if not (x==i and y==j):
							D[x][y] -= 1
							qq.add((x, y))
	return D, qq


def printM(M, name):
	print(name + ':')
	for row in M:
		l=''
		for c in row:
			l+=str(c)
		print(l)


with open("input.txt", "r") as file:
	lines = file.readlines()
	matrix = []
	for line in lines:
		matrix.append([c for c in line.strip()])
	n = len(matrix)		# 93
	m = len(matrix[0])	# 94
	counts = [[0 for mm in range(m)] for nn in range(n)]  # 1st gen no occupied seats
	# positions to inspect
	queue = set()
	for i in range(n):
		for j in range(m):
			queue.add((i, j))

	gen_count = 0
	while len(queue) > 0:
		print('round', gen_count, 'qq size', len(queue))
		next_counts, next_queue = evolve(matrix, counts, queue, n, m)
		gen_count += 1
		# printM(matrix, 'matrix')
		# printM(next_counts, 'next counts')
		counts = next_counts
		queue = next_queue

	if len(next_queue) == 0:
		final_count = 0
		for row in matrix:
			for c in row:
				if c == '#':
					final_count += 1
		print('final_count', final_count)
