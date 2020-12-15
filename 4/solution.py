req_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} # "cid" optional
valid_count = 0

with open("input.txt", "r") as file:
	lines = file.read().split("\n\n")
	debug = True
	for line in lines:
		line = line.replace("\n", " ")
		kv_pairs = line.split(" ")
		keys = set([kv.split(":")[0] for kv in kv_pairs])
		if debug:
			print(line)
			print(kv_pairs)
			print(keys)
			debug = False
		if keys.issuperset(req_keys):
			valid_count += 1
	print(str(valid_count))

