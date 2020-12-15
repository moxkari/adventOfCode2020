with open("input.txt", "r") as inn:
	lines = inn.readlines()
	valid_count = 0
	for line in lines:
		rule, pwd = line.split(": ")
		bounds, letter = rule.split(" ")
		lb, ub = bounds.split("-")
		if int(lb) <= pwd.count(letter) <= int(ub):
			valid_count += 1
			print(pwd)
	print(str(valid_count))
