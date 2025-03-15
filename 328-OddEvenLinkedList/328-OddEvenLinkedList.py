# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        if head.next == None:
            return head
        
        even_head = head
        odd_head = head.next
        
        even_curr = even_head
        odd_curr = odd_head
        
        appended = False
        
        while odd_curr != None:
            if odd_curr.next != None:
                even_curr.next = odd_curr.next
                even_curr = even_curr.next

                if even_curr != None:
                    odd_curr.next = even_curr.next
                    odd_curr = odd_curr.next
                    
            else:
                even_curr.next = odd_head
                appended = True
                break
        
        if not appended:
            even_curr.next = odd_head
        
        return even_head
            
        