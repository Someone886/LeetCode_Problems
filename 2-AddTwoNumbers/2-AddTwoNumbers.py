# Last updated: 4/6/2025, 12:59:56 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_over = 0

        curr_1 = l1
        curr_2 = l2
        dummy = ListNode()
        prev = dummy

        while curr_1 != None and curr_2 != None:
            new_node = ListNode(curr_1.val + curr_2.val + carry_over)
            carry_over = 0

            if new_node.val >= 10:
                carry_over = 1
                new_node.val -= 10
            
            prev.next = new_node
            
            prev = prev.next
            curr_1 = curr_1.next
            curr_2 = curr_2.next
        
        while curr_1 != None:
            new_node = ListNode(curr_1.val + carry_over)
            carry_over = 0

            if new_node.val >= 10:
                carry_over = 1
                new_node.val -= 10

            prev.next = new_node

            prev = prev.next
            curr_1 = curr_1.next
        
        while curr_2 != None:
            new_node = ListNode(curr_2.val + carry_over)
            carry_over = 0

            if new_node.val >= 10:
                carry_over = 1
                new_node.val -= 10
            
            prev.next = new_node

            prev = prev.next
            curr_2 = curr_2.next
        
        if carry_over == 1:
            new_node = ListNode(carry_over)
            carry_over = 0
            prev.next = new_node
        
        return dummy.next