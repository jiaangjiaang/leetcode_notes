class Solution:
    def romanToInt(s):
        sum = 0
        high_level = 0
        mapping = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        for i in s[::-1]:
            level = mapping[i]
            if level >= high_level:
                sum += level
                high_level = level
            elif level < high_level:
                sum -= level
        return sum