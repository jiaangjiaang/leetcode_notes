class Solution:
    def firstBadVersion(n):
        while 1:
            mid = n//2
            if isBadVersion(mid):
                return mid
            else:
                mid = mid//2
