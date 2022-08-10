class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        current = head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous