class ListNode:
     def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers(l1, l2):
        dummy = p = ListNode(None)
        sum = 0
        while l1 or l2 or sum != 0:
            sum += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            print("l1+l2")
            print(sum)
            p.next = ListNode(sum%10)
            print("p.next")
            print(p.next.val)
            p = p.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            sum = sum //10
            print("//10")
            print(sum)
        return dummy.next

if __name__ == "__main__":
    node1 = ListNode(9)
    node2 = ListNode(9)
    node3 = ListNode(9)
    node4 = ListNode(9)
    node5 = ListNode(9)

    node1.next = node2
    node2.next = node3

    node4.next = node5
    final = Solution.addTwoNumbers(node1, node4) 
    print(final.val)
    print(final.next.val)
    final = final.next
    print(final.next.val)
    final = final.next
    print(final.next.val)
