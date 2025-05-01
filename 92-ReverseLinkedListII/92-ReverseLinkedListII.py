# Last updated: 4/30/2025, 10:38:32 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        cur = dummy_head
        index = 0

        while index < left - 1:
            cur = cur.next
            index += 1
        
        # cur now points to the node before left

        left = cur.next
        left_next = left.next
        index += 1

        while index < right:
            left_next_next = left_next.next
            left_next.next = left

            left = left_next
            left_next = left_next_next

            index += 1
        
        cur.next.next = left_next
        cur.next = left
        
        return dummy_head.next
        
