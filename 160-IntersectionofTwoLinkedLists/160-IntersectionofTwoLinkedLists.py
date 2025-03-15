# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr_a = headA
        curr_b = headB

        len_a = 1
        len_b = 1

        while curr_a.next != None:
            len_a += 1
            curr_a = curr_a.next
        
        while curr_b.next != None:
            len_b += 1
            curr_b = curr_b.next
        
        if curr_a != curr_b:
            return None
        
        len_diff = len_a - len_b
        curr_a = headA
        curr_b = headB

        if len_diff > 0:
            for i in range(len_diff):
                curr_a = curr_a.next
        
        elif len_diff < 0:
            for i in range(abs(len_diff)):
                curr_b = curr_b.next
        
        while curr_a != curr_b:
            curr_a = curr_a.next
            curr_b = curr_b.next
        
        return curr_a