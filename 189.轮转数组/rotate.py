class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            self.trans(nums)

    def trans(self, nums):
        nums_len = len(nums)
        for i in range(nums_len - 1, 0, -1):
            temp = nums[i - 1]
            nums[i - 1] = nums[i]
            nums[i] = temp

