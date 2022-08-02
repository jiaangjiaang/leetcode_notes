class Solution:
    def sortedSquares(nums):
        nums_len = len(nums)
        new_list = [0] * nums_len
        left = 0
        right = nums_len - 1
        new_list_pos = nums_len - 1
        while left <= right:
            if nums[left] * nums[left] < nums[right] * nums[right]:
                new_list[new_list_pos] = nums[right] * nums[right]
                right -= 1
            else:
                new_list[new_list_pos] = nums[left] * nums[left]
                left += 1
            new_list_pos -= 1
        return new_list