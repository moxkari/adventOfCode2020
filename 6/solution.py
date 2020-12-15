with open("input.txt", "r") as file:
	groups = file.read().split("\n\n")
	count_total = 0
	for group in groups:
		line = group.replace("\n", "").strip()
		line_dict = dict.fromkeys(line, 0)
		count_total += len(line_dict)
	print(count_total)
