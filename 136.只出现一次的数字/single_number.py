class Solution:
    def singleNumber(nums):
        ans = 0
        for num in nums:
            ans ^= num
        return ans

a = [2,2,1]
print(Solution.singleNumber(a))