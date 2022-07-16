class Solution:
    def searchInsert(nums, target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if target > nums[-1]:
                return len(nums)
            else:
                for i in range(len(nums)):
                    if nums[i] >= target:
                        return i
