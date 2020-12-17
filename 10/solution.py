with open("input.txt", "r") as file:
	nums = [int(i.strip()) for i in file.readlines()]
	nums.sort()
	diffs = dict()
	# for first connection
	diffs[nums[0]] = 1
	for i in range(1, len(nums)):
		diff = nums[i] - nums[i-1]
		diffs[diff] = diffs.get(diff, 0) + 1
	# for last connection
	diffs[3] += 1
	print(diffs[1]*diffs[3])