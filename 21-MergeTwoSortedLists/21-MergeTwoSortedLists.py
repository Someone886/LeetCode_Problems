# Last updated: 4/5/2025, 4:52:31 PM
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        curr_node = dummy_head
        
        curr_1 = list1
        curr_2 = list2

        while curr_1 != None and curr_2 != None:
            if curr_1.val <= curr_2.val:
                curr_node.next = curr_1
                curr_1 = curr_1.next
            else:
                curr_node.next = curr_2
                curr_2 = curr_2.next
            
            curr_node = curr_node.next
        
        if curr_1 == None:
            curr_node.next = curr_2
        elif curr_2 == None:
            curr_node.next = curr_1
        
        return dummy_head.next