class Solution:
    '''
    此题使用双指针的思路
    在数组中设置两个指针
    判断两个指针指向的数是否相同，如果不同，将右指针的数左移覆盖重复数
    '''
    def removeDuplicates(nums, val):
        right = 0
        left = 0
        while left < len(nums):
            if nums[left] != val:
                nums[right] = nums[left]
                right += 1
            left += 1
        return right

if __name__ == "__mian__":
    nums = [0, 1, 2, 3, 3, 4]
    print(Solution.removeDuplicates(nums))