class Solution:
    def moveZeroes(nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            while nums[i] == 0 and i != len(nums) - 1:
                temp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = temp