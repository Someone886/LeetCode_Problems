# Last updated: 6/22/2025, 2:53:32 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        def reverse(head, k):
            cnt = 0
            curr = head
            while curr != None and cnt < k:
                cnt += 1
                curr = curr.next
            
            if cnt < k:
                return head, None

            prev, curr = None, head
            cnt = 0

            while curr != None and cnt < k:
                nxt = curr.next
                curr.next = prev
                
                prev = curr
                curr = nxt

                cnt += 1
            
            return prev, curr
        
        dummy_head = ListNode()
        curr_head = dummy_head
        last_head = head

        while True:
            this_head, next_head = reverse(last_head, k)

            curr_head.next = this_head
            curr_head = last_head
            
            last_head = next_head
            
            if last_head == None:
                break
        
        return dummy_head.next
        