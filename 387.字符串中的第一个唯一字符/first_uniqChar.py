class Solution:
    def firstUniqChar(s):
        for i in range(len(s)):
            if s[i] not in s[i+1:] and s[i] not in s[:i]:
                return i
        return -1

s = "loveleetcode"

print(Solution.firstUniqChar(s))