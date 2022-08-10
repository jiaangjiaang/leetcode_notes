class Solution:
    def isPalindrome(self, head) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        nums_len = len(nums)
        left = nums_len // 2 - 1
        right = 0
        if nums_len % 2 == 0:
            right = left + 1
        else:
            right = left + 2
        while left >= 0:
            if nums[left] == nums[right]:
                left -= 1
                right += 1
            else:
                return False
        return True