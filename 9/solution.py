with open("input.txt", "r") as file:
	window = 25
	lines = [int(i.strip()) for i in file.readlines()]
	sums = dict()
	# construct init map
	for j in range(window):
		for k in range(window):
			if j != k:
				s = lines[j] + lines[k]
				sums[s] = sums.get(s, 0) + 1

	# roll the window
	for m in range(window, len(lines)):
		incoming = lines[m]
		outgoing = lines[m-window]
		if incoming not in sums:
			print(str(incoming) + ' BROKE THE THING')
			break
		for n in range(m-window+1, m):
#			print('m=', m, ', n=', n, 'incoming=', incoming, 'outgoing=', outgoing)
			incoming_sum = incoming + lines[n]
			sums[incoming_sum] = sums.get(incoming_sum, 0) + 1
			outgoing_sum = outgoing + lines[n]
			sums[outgoing_sum] = sums[outgoing_sum] - 1
