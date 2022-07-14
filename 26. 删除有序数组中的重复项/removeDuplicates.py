class Solution:
    '''
    此题使用双指针的思路
    在数组中设置两个指针
    判断两个指针指向的数是否相同，如果不同，将右指针的数左移覆盖重复数
    '''
    def removeDuplicates(nums):
        p = 0
        q = 0
        num = 0
        while q < len(nums):
            if nums[p] != nums[q]:
                p += 1
                nums[p] = nums[q]
            q = q+1
        return p+1

if __name__ == "__mian__":
    nums = [0, 1, 2, 3, 3, 4]
    print(Solution.removeDuplicates(nums))