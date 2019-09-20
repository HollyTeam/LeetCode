# 1.较优的方案：两个set分别存储已经遍历过的以及nums中两个数绝对值差为k的较小的那个数
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        saw, diff = set(), set()
        for i in nums:
            # 注意，这里虽然saw一开始为空集合，比如i=1,k=2，接下来只要遍历到i=3，i-k=1就会被添加到diff集合中
            if i-k in saw:
                diff.add(i-k)
            if i+k in saw:
                diff.add(i)
            saw.add(i)
        return len(diff)


# 2.用字典存储数字出现的次数。判断nums[i]+k在不在set(nums)中
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        nums_set = set(nums)
        if k < 0:
            return 0
        elif k == 0:
            # each_num:times
            count_dict = {}
            for each in nums:
                if each not in count_dict.keys():
                    count_dict[each] = 1
                else:
                    count_dict[each] += 1

            for key in nums_set:
                if count_dict[key] >= 2:
                    res += 1

        # k>0
        else:
            for key in nums_set:
                if (key + k) in nums:
                    res += 1

        return res
