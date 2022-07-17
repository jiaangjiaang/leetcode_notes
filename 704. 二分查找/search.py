class Solution:
    def search(nums, target):
        left_pointer = 0
        right_pointer = len(nums) - 1
        while (left_pointer <= right_pointer):
            mid = (right_pointer - left_pointer)//2 + left_pointer
            mid_num = nums[mid]
            if mid_num == target:
                return mid
            elif mid_num > target:
                right_pointer = mid - 1
            else:
                left_pointer = mid + 1
        return -1