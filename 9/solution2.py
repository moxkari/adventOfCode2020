with open("input.txt", "r") as file:
	magic_sum = 69316178
	nums = [int(i.strip()) for i in file.readlines()]
	for i in range(len(nums)):
		# explore all seqs with i as lower bound
		sum_i = nums[i]
		smallest = nums[i]
		largest = nums[i]
		for j in range(i+1, len(nums)):
			sum_i += nums[j]
			smallest = min(nums[j], smallest)
			largest = max(nums[j], largest)
			if sum_i == magic_sum:
				print('DONE!', smallest+largest)
				break

