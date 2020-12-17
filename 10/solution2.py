def subtree(i, nums):
	print('subtree i=', i, ',', nums[i])
	if memo[i]:
		return memo[i]
	if i==n-1: # last adapter
		return memoize(i, 1)
	elif i==n-2:
		return memoize(i, 1)
	# can we skip next two?
	if i+3 < n:
		if nums[i+3]-nums[i] <= 3:
			# 3 branches
			return memoize(i, subtree(i+1, nums) + subtree(i+2, nums) + subtree(i+3, nums))
	if i+2 < n:
		if nums[i+2]-nums[i] <= 3:
			# 2 branches
			return memoize(i, subtree(i+1, nums) + subtree(i+2, nums))
		else:	# no branching
			return memoize(i, subtree(i+1, nums))
	
def memoize(j, solution):
	memo[j] = solution
	print('memo', j, '=', solution)
	return solution

# 6908379398144 close
# 12089663946752 also close wtf
# 5181284548608 not it

if __name__ == '__main__':
	with open("input.txt", "r") as file:
		nums = [int(l.strip()) for l in file.readlines()]
		nums.sort()
		# think i'm abusing var names here but w/e im on vacation
		n = len(nums)
		memo = [None]*n
		print(subtree(0, nums))

