class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 构造字典
        index = []
        for i in range(len(nums)):
            index.append(i)
        my_dict = dict(zip(nums, index)) # 键为nums,值为index,这样就能根据nums[i]得到 索引值i

        for i in range(len(nums)):
            curr = nums[i]
            dvalue = target - curr

            if dvalue in my_dict.keys():
                result = [my_dict.get(dvalue), i]
                if len(set(result)) == 1:
                    continue
                result.sort()
                return result

        return None