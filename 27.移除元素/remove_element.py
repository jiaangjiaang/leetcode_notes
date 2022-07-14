class Solution:
    def removeElement(nums, val):
        q = 0
        p = 0
        while p < len (nums):
            if nums[q] != val:
                q += 1    
            else:
                nums[q] = nums[p]
'''
    此题依然使用双指针的思路
'''
