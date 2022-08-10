class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        current = nodere
        previous = node
        current.val = current.next.val
        while current.next != None:
            previous = current
            current.val = current.next.val
            current = current.next
        previous.next = None

