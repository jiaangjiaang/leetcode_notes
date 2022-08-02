class Solution:
    def removeElement(nums, val):
        right = 0
        left = 0
        while left < len(nums):
            if nums[left] != val:
                nums[right] = nums[left]
                right += 1
            left += 1
        return right
'''
    此题依然使用双指针的思路
'''
