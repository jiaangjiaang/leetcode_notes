class Solution:
    def intersect(nums1, nums2):
        n1_len = len(nums1)
        n2_len = len(nums2)
        result = []
        if n1_len >= n2_len:
            for i in nums2:
                if i in nums1:
                    nums1.remove(i)
                    result.append(i)
        else:
            for i in nums1:
                if i in nums2:
                    nums2.remove(i)
                    result.append(i)
        return  result

a = [1, 2]
b = [1, 1]
print(Solution.intersect(a, b))