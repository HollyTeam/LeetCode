def findMedianSortedArrays(nums1, nums2):
	nums = nums1 + nums2
	nums_len = len(nums)
	nums.sort()
	if nums_len % 2 == 0:
		result = (nums[nums_len//2 - 1] + nums[nums_len//2])/2
		return result
	else:
		return nums[nums_len//2]

nums1 = [1, 3]
nums2 = [2]
result = findMedianSortedArrays(nums1, nums2)
print(result)