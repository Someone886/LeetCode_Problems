# Last updated: 4/5/2025, 8:55:20 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def reverseList(head: Optional[ListNode]):
            prev, curr = None, head

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                
            return prev
            
        if head == None:
            return
        
        slow, fast = head, head
        prev_slow = None

        while fast and fast.next != None:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev_slow == None:
            return
        
        prev_slow.next = None

        l1 = head
        l2 = slow
        
        l2 = reverseList(l2)

        while l1 != None:
            temp_1 = l1.next
            temp_2 = l2.next

            l1.next = l2
            if temp_1 != None:
                l2.next = temp_1

            l1 = temp_1
            l2 = temp_2