class Solution:
    def lengthOfLongestSubstring(s):
        s_len = len(s)
        if s_len == 0:
            return 0
        if s_len == 1:
            return 1
        longest_lenth = 0
        lenth = 1
        for left in range(s_len - 1):
            right = left + 1
            while right < s_len and s[right] not in s[left:right]:
                lenth += 1
                right += 1
            if lenth > longest_lenth:
                longest_lenth = lenth
            lenth = 1
        return longest_lenth

s = " "
print(s==None)
#print(Solution.lengthOfLongestSubstring(s))