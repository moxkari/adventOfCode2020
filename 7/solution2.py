import re

bag_count_re = re.compile("^\d+\s")

def do_subtree(root, bag_dict):
	count = 0
	for raw_v in bag_dict[root]:
		if raw_v != 'no other bags':
			sub_count = int(bag_count_re.match(raw_v)[0])
			sub_root =  bag_count_re.split(raw_v)[1].rstrip('s')
			count += sub_count
			count += sub_count * do_subtree(sub_root, bag_dict)
	return count


if __name__ == '__main__':
	with open("input.txt", "r") as file:
		lines = file.readlines()
		bag_dict = dict()

		for line in lines:
			key, raw_vals = line.strip('.\n').split("s contain ")
			vals = raw_vals.split(", ")
			bag_dict[key] = vals
			
		root = 'shiny gold bag'
		print(len(bag_dict))
		print(do_subtree(root, bag_dict))