class Solution:
    def maxUncrossedLines(self, nums1, nums2) -> int:
        sum = 0
        top, down = 0, 0
        while top <= len(nums1)-1 and down <= len(nums2)-1:
            if nums1[top] != nums2[down]:
                down += 1
            if nums1[top] == nums2[down]:
                sum += 1
                top += 1
                down += 1
        return sum
