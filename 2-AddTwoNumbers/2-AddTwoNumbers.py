# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans_head = ListNode()
        curr = ans_head
        
        add_extra = 0
        
        l1_head = l1
        l2_head = l2
        
        while l1_head != None or l2_head != None:
            node_sum = 0
            
            if l1_head != None:
                node_sum += l1_head.val
                l1_head = l1_head.next
            
            if l2_head != None:
                node_sum += l2_head.val
                l2_head = l2_head.next
            
            node_sum += add_extra
            
            add_extra = node_sum // 10            
            node_sum -= (add_extra * 10) 
            
            ans_node = ListNode(node_sum)
            curr.next = ans_node
            
            curr = ans_node
        
        if add_extra:
            ans_node = ListNode(add_extra)
            curr.next = ans_node
        
        return ans_head.next