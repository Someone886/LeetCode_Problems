# Last updated: 4/14/2025, 3:33:20 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None

        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return None
            
            node_copy = Node(node.val)
            old_to_new[node] = node_copy

            neighbors_copy = []
            for neighbor in node.neighbors:
                neighbor_copy = dfs(neighbor)
                if neighbor_copy == None:
                    neighbor_copy = old_to_new[neighbor]
                else:
                    old_to_new[neighbor] = neighbor_copy
                neighbors_copy.append(neighbor_copy)
            node_copy.neighbors = neighbors_copy
        
            return node_copy
        
        dfs(node)
        return old_to_new[node]
        