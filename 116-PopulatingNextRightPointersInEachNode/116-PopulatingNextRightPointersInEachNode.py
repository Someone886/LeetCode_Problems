# Last updated: 6/22/2025, 2:52:32 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return None
        
        this_level = [root]
        next_level = []

        while len(this_level) != 0:
            for i in range(1, len(this_level)):
                this_level[i-1].next = this_level[i]
            
            for node in this_level:
                if node.left != None:
                    next_level.append(node.left)
                if node.right != None:
                    next_level.append(node.right)
            
            this_level = next_level
            next_level = []

        return root