class Solution:
    def mergeTwoLists(list1, list2):
        l1_pointer = 0
        l2_pointer = 0
        l1_len = len(list1)
        l2_len = len(list2)
        l1_current = list1.head
        l2_current = list2.head
        if l1_len == 0 and l2_len == 0:
            return list1
        elif l1_len == 0 and l2_len != 0:
            return l2_len
        elif l1_len != 0 and l2_len == 0:
            return l1_len
        if l1_len >= l2_len:
            for i in range(l2_len):
                if l1_current >= l2_current:
                    l1_current.next = l2_current


#递归
#递归