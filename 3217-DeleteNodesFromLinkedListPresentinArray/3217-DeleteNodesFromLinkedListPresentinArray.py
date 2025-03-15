# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        set_nums = set(nums)
        
        while head and head.val in set_nums:
            head = head.next 

        if head is None:
            return

        current_node = head
        next_node = head.next

        while next_node is not None:
            if next_node.val in set_nums:
                current_node.next = next_node.next
                next_node = next_node.next
            else:
                current_node = current_node.next
                next_node = next_node.next
            
        return head