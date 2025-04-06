# Last updated: 4/5/2025, 11:25:03 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        curr = head
        while curr != None:
            length += 1
            curr = curr.next
        
        n_from_left = length - n
        if n_from_left == 0:
            return head.next

        prev, curr = None, head

        while n_from_left > 0:
            prev = curr
            curr = curr.next
            n_from_left -= 1

        prev.next = curr.next

        return head
        