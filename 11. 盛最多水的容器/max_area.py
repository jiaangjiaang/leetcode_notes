class Solution:
    def maxArea(height):
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            ans = min(height[left], height[right]) * (right - left)
            max_area = max(ans, max_area)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return max_area