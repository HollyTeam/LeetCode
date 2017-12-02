class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

#         len_s = len(s)
#         for i in range(len_s, 0, -1):
#             for j in range(0, len_s-i+1):
#                 sub_str = s[j:(j+i)]
#                 if len(set(sub_str)) == i:
#                     return i

#         return 0
        if len(s) == 0:
            return 0
        my_dict = dict()
        my_max = 0
        j = 0
        for i in range(len(s)):
            if s[i] in my_dict.keys():
                j = max(j, my_dict[s[i]] + 1)
            my_dict[s[i]] = i
            my_max = max(my_max, i-j+1)
        return my_max