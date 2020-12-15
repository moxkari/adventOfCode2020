with open("input.txt", "r") as inn:
	lines = inn.readlines()
	valid_count = 0
	for line in lines:
		rule, pwd = line.split(": ")
		indices, letter = rule.split(" ")
		i1, i2 = indices.split("-")
		p1, p2 = pwd[int(i1)-1], pwd[int(i2)-1]
		if (p1 == letter and p2 != letter) or (p2 == letter and p1 != letter):
			valid_count += 1
			print(pwd)
	print(str(valid_count))
