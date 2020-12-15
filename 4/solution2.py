import re

req_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} # "cid" optional
valid_count = 0

regex_year = re.compile("^\d{4}$")
regex_hgt  = re.compile("^\d+(cm|in)$")
regex_hgt_cm = re.compile("^\d+(cm)$")
regex_hcl =  re.compile("^#[a-f0-9]{6}$")
valid_ecl =  {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
regex_pid =  re.compile("^\d{9}$")
with open("input.txt", "r") as file:
	lines = file.read().split("\n\n")
	print(len(lines))
	for line in lines:
		line = line.replace("\n", " ").strip()
		kv_pairs = line.split(" ")
		try:
			pass_dict = dict([kv.split(":") for kv in kv_pairs])
		except Exception as e:
			print(line)
			raise
		if set(pass_dict.keys()).issuperset(req_keys):
			try:
				# validate each field			
				# year fields:  byr, iyr, eyr
				byr = int(regex_year.match(pass_dict["byr"])[0])
				iyr = int(regex_year.match(pass_dict["iyr"])[0])
				eyr = int(regex_year.match(pass_dict["eyr"])[0])
				if (1920 <= byr <= 2002) and (2010 <= iyr <= 2020) and (2020 <= eyr <= 2030):
					# hgt
					valid_hgt = False
					hgt_str = pass_dict["hgt"]
					if regex_hgt.match(hgt_str):
						if regex_hgt_cm.match(hgt_str):
							valid_hgt = 150 <= int(hgt_str.split("cm")[0]) <= 193
						else:
							valid_hgt = 59 <= int(hgt_str.split("in")[0]) <= 76
						if valid_hgt:
							if regex_hcl.match(pass_dict["hcl"]):
								if pass_dict["ecl"] in valid_ecl:							
									if regex_pid.match(pass_dict["pid"]):
										valid_count += 1
						else:
							print("illegal hgt: " + pass_dict["hgt"])
			except Exception as e:
				print(e)

	print(str(valid_count))

