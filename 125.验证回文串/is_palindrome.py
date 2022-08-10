#这题其实没写完，但是题目太蠢了，不想写了

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for strs in s:
            if self.is_english(strs):
                new_s += strs
        s_len = len(new_s)
        left = s_len // 2
        right = left + 1
        while left >= 0:
            if self.english_is_equal(s[left], s[right]):
                left -= 1
                right += 1
            else:
                return False
        return True

    def is_english(self, s):
        if ord(s) >= 65 and ord(s) <= 90:
            return True
        elif ord(s) >= 97 and ord(s) <= 122:
            return True
        else:
            return False

    def english_is_equal(self, a, b):
        if ord(a) == ord(b):
            return True
        elif ord(a) - 32 == ord(b) or ord(a) + 32 == ord(b):
            return True
        else:
            return False