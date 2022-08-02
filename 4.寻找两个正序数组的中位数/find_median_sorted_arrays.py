class Solution:
    def findMedianSortedArrays(nums1, nums2):
        m_len = len(nums1)
        n_len = len(nums2)
        total_len = m_len + n_len
        total_list = []
        for i in nums1:
            total_list.append(i)
        for i in nums2:
            total_list.append(i)
        total_list.sort()
        if total_len % 2 == 0:
            index = total_len // 2
            return (total_list[index-1] + total_list[index])/2
        else:
            return total_list[(total_len-1)//2]


if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [3,4]