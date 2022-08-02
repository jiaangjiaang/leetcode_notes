from leetcode_notes.list_node import ListNode
'''
此题的思路是使用快慢指针。慢指针移动一次，快指针移动两次，如果链表存在环，则快慢指针就一定会相遇。
当快指针的next为空说明链表到头了，那么链表就没有环形结构
'''

class Solution:
    def hasCycle(head) -> bool:
        if not head or not head.next:
            return False
        slow_pointer = head
        fast_pointer = head.next
        while slow_pointer != fast_pointer:
            if not fast_pointer or not fast_pointer.next:
                return False
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return True
