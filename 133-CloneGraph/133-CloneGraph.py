# Last updated: 12/28/2025, 2:21:03 AM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val = 0, neighbors = None):
5        self.val = val
6        self.neighbors = neighbors if neighbors is not None else []
7"""
8
9from typing import Optional
10class Solution:
11    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
12        if node == None:
13            return None
14
15        old_to_new = {}
16
17        def dfs(node):
18            # already visited, do not create new copy and mapping
19            if node in old_to_new:
20                return old_to_new[node]
21            
22            # not visited yet, create new copy and mapping
23            node_copy = Node(node.val)
24            old_to_new[node] = node_copy
25
26            neighbors_copy = []
27            for neighbor in node.neighbors:
28                neighbor_copy = dfs(neighbor)
29                neighbors_copy.append(neighbor_copy)
30            node_copy.neighbors = neighbors_copy
31        
32            return node_copy
33        
34        dfs(node)
35        return old_to_new[node]
36        