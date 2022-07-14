class Solution:
    def mergeTwoLists(list1, list2):
        current = list1.head
        for i in range(len(list1)):
            current = current.next
        current.next = list2.head
        for i in range(len(list1) - 1):
            for j in range(len(list1) - 1 -i):
                if
#递归
#递归