with open("input", "r") as inn:
	lines = inn.readlines()
	nums = [int(l.strip()) for l in lines]
	#for n in nums:
	#	print(str(n))
	for i in range(0,len(lines)):
		for j in range(i+1,len(lines)):
			ni=nums[i]
			nj=nums[j]
			if ni+nj==2020:
				print(ni*nj)
	print('welp')