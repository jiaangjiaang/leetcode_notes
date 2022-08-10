class Solution:
    def mergeTwoLists(list1, list2):
       prehead = ListNode(-1)
       previous = prehead
       while list1 and list2:
           if list1.val <= list2.val:
               previous.next = list1
               list1 = list1.next
           else:
               previous.next = list2
               list2 = list2.next
           previous = previous.next
       previous.next = list1 if list1 is not None else list2
       return prehead.next
       
