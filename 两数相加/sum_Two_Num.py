from operator import le
from typing import List


"""
两层暴力循环，太慢，太占内存。
class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return[i,j]
"""






if __name__ == "__main__":
    Solution.twoSum([3,2,3], 6)