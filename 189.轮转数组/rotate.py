class Solution:
    def rotate(nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            temp = nums[n-1]
            nums[n-1] = nums[i]
            nums[n] = temp