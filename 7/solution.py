import re

with open("input.txt", "r") as file:
	lines = file.readlines()
	bag_dict = dict()
	final_bag_candidates = set()
	bag_candidates = set()
	total_count = 0
#	debug = True
	# first pass: construct bag map
	for line in lines:
		key, raw_vals = line.strip('.\n').split("s contain ")
		vals = [re.sub('^\d+\s', '', raw_val).rstrip('s') for raw_val in raw_vals.split(", ")]
		# if debug:
		# 	print(vals)
		# 	debug=False
		bag_dict[key] = vals
		if 'shiny gold bag' in vals:
			bag_candidates.add(key)

	while len(bag_candidates) > 0:
		print("bag_candidates: " + str(bag_candidates))
		next_level_bag_candidates = set()
		for b in bag_candidates:
			final_bag_candidates.add(b)
			for e in bag_dict.keys():
				# should've built this inverted, but oh well
				if b in bag_dict[e]:
					next_level_bag_candidates.add(e)

		bag_candidates = next_level_bag_candidates

	print("final_bag_candidates: " + str(final_bag_candidates))
	print(len(final_bag_candidates))