# Last updated: 5/31/2025, 11:17:08 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def _calculate_gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        if head == None:
            return head
        
        curr, nxt = head, head.next

        while curr != None and nxt != None:
            gcd = _calculate_gcd(curr.val, nxt.val)
            new_node = ListNode(gcd, nxt)
            curr.next = new_node
            curr = nxt
            nxt = nxt.next

        return head