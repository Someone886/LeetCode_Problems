# Last updated: 4/7/2025, 12:30:44 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None or len(lists) == 0:
            return None

        val_map = {}
        node_map = {}
        heap = []
        k = len(lists)
        dummy_head = ListNode()
        curr = dummy_head
        
        order = 0

        while True:
            for i in range(k):
                if i not in node_map:
                    node_map[i] = lists[i]
                
                node = node_map[i]
                if node == None:
                    continue
                    
                order += 1
                pair = (node.val, order, node)
                heapq.heappush(heap, pair)

                node_map[i] = node.next
            
            if not heap:
                break

            next_node_val, _, next_node = heapq.heappop(heap)

            curr.next = next_node
            curr = curr.next
        
        return dummy_head.next
        