# Last updated: 4/6/2025, 12:38:15 AM
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head
        
        dummy = Node(0)
        hash_map = {}

        prev = dummy
        curr = head

        while curr:
            if curr in hash_map:
                new_node = hash_map[curr]
            else:
                new_node = Node(curr.val)
                hash_map[curr] = new_node
            
            prev.next = new_node
            
            if curr.random != None:
                if curr.random not in hash_map:
                    new_random_node = Node(curr.random.val)
                    hash_map[curr.random] = new_random_node
                
                new_node.random = hash_map[curr.random]

            curr = curr.next
            prev = prev.next
        
        return dummy.next
        