# 给定一个字符串，找到其中的一个最长的字串，使得这个子串不包含重复的字符
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

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

s = "abcabcbb"
result = lengthOfLongestSubstring(s)
print("result:  ", result)