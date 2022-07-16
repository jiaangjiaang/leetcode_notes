class Solution:
    def merge(nums1, m, nums2, n):
        nums1_pointer = 0
        nums2_pointer = 0
        new_list = []
        while nums1_pointer < m or nums2_pointer < n:
            if nums1_pointer == m:
                new_list.append(nums2[nums2_pointer])
                nums2_pointer += 1
            elif nums2_pointer == n:
                new_list.append(nums1[nums1_pointer])
                nums1_pointer += 1
            elif nums1[nums1_pointer] < nums2[nums2_pointer]:
                new_list.append(nums1[nums1_pointer])
                nums1_pointer += 1
            else:
                new_list.append(nums2[nums2_pointer])
                nums2_pointer += 1
        nums1[:] = new_list