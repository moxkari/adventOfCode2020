with open("input", "r") as inn:
	lines = inn.readlines()
	nums = [int(l.strip()) for l in lines]
	#for n in nums:
	#	print(str(n))
	for i in range(0,len(lines)):
		for j in range(i+1,len(lines)):
			for k in range(j+1,len(lines)):
				ni=nums[i]
				nj=nums[j]
				nk=nums[k]
				if ni+nj+nk==2020:
					print(ni*nj*nk)
	print('welp')