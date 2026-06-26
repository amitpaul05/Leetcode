# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode()
        tail = l
        c = 0
        while l1 or l2:
            if l1.val is None and l2.val is None:
                if c:
                    tail.next = ListNode(c)
                    tail = tail.next
                return l.next

            s = ((l1.val if l1.val else 0) + (l2.val if l2.val else 0) + c) % 10
            c = ((l1.val if l1.val else 0) + (l2.val if l2.val else 0) + c) // 10

            tail.next = ListNode(s)
            tail = tail.next
            
            if l1.next:
                l1 = l1.next
            else:
                l1.val = None
            if l2.next:
                l2 = l2.next
            else:
                l2.val = None
        return l.next