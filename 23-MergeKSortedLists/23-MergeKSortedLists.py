# Last updated: 6/22/2025, 2:53:33 PM
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
        heap = []
        k = len(lists)
        dummy_head = ListNode()
        curr = dummy_head
        
        order = 0

        for i in range(k):
            node = lists[i]
            if node == None:
                continue

            pair = (node.val, order, node)
            order += 1
            heapq.heappush(heap, pair)

        while heap:
            next_node_val, _, next_node = heapq.heappop(heap)

            curr.next = next_node
            curr = curr.next

            if next_node.next != None:
                pair = (next_node.next.val, order, next_node.next)
                order += 1
                heapq.heappush(heap, pair)
        
        return dummy_head.next
        