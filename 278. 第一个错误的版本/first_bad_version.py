class Solution:
    def firstBadVersion(n):
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

