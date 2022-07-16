#这个解法，太垃圾，明天研究一下

class Solution:
    def containsDuplicate(nums):
        flag = False
        num_dcit = dict()
        for i in nums:
            if i not in num_dcit.keys():
                num_dcit[i] = 1
            else:
                num_dcit[i] = 2
        for value in num_dcit.values():
            if value > 1:
                flag = True
        return flag
nums = [2,14,18,22,22]
print(Solution.containsDuplicate(nums))