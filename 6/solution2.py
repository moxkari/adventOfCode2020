with open("input.txt", "r") as file:
	groups = file.read().split("\n\n")
	count_total = 0
	debug = True
	for g in range(len(groups)):
		debug = g > len(groups)-2
		group = groups[g]
		if debug:
			print(group)
		line_dicts = [dict.fromkeys(line, 0) for line in group.strip().split("\n")]
		if debug:
			for ld in line_dicts:
				print(ld.keys())
		for k in line_dicts[0].keys():
			if debug:
				print("k: " + k)
			everyone = True
			for i in range(len(line_dicts)):
				everyone = everyone and (k in line_dicts[i])
				if everyone and i==len(line_dicts)-1:
					if debug:
						print("everyone has " + k)
					count_total += 1
		if debug:
			print("after round: " + str(count_total))


	print(count_total)
