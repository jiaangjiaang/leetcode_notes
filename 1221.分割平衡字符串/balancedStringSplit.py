class Solution:
    def balancedStringSplit(self, s: str) -> int:
        '''
        使用栈的一种解法。
        num = 0
        stack = []
        stack.append(s[0])
        for ch in s[1:]:
            if len(stack) == 0 or ch == stack[-1]:
                stack.append(ch)
            if ch != stack[-1]:
                stack.pop()
            if len(stack) == 0:
                num += 1
        return num
        '''
        #下面是贪心算法
        p, q = 0, 0
        for ch in s:
            if ch == 'L':
                q += 1
            else:
                q -= 1
            if q == 0:
                p += 1
        return p