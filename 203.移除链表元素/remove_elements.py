from leetcode_notes.list_node import ListNode
class Solution:
    def removeElements(head, val) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        p = dummy
        while p is not None:
            if p.next and p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next