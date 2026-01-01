# Last updated: 1/1/2026, 6:13:03 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
10        # 1. Map each node to its parent
11        parent_map = {}
12        def find_parents(node, par=None):
13            if node:
14                parent_map[node] = par
15                find_parents(node.left, node)
16                find_parents(node.right, node)
17        
18        find_parents(root)
19        
20        # 2. Level-by-Level BFS
21        dq = deque([target])
22        visited = {target}
23        dist_so_far = 0
24
25        while dq:
26            # If we've reached the distance k, the entire queue is our answer
27            if dist_so_far == k:
28                return [node.val for node in dq]
29            
30            # Process the current "level" entirely
31            for _ in range(len(dq)):
32                node = dq.popleft()
33                
34                # Check all 3 directions: Left, Right, and Up (Parent)
35                for neighbor in [node.left, node.right, parent_map[node]]:
36                    if neighbor and neighbor not in visited:
37                        visited.add(neighbor)
38                        dq.append(neighbor)
39            
40            # Move to the next distance level
41            dist_so_far += 1
42                        
43        return []
44
45# from collections import deque
46
47# class Solution:
48#     def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
49#         if not root or not target:
50#             return []
51#         # Early exit for distance 0 (target is the only answer)
52#         if k == 0: 
53#             return [target.val]
54
55#         # Adjacency list to treat the tree as an undirected graph
56#         graph = {}
57
58#         def dfs_graph_builder(node, pre_node):
59#             # Potential Bug: if node values are not unique, 
60#             # this will overwrite or merge unrelated nodes.
61#             if node.val not in graph:
62#                 graph[node.val] = []
63            
64#             # Connect current node to parent
65#             if pre_node:
66#                 graph[node.val].append(pre_node.val)
67
68#             # Connect current node to left child
69#             if node.left:
70#                 graph[node.val].append(node.left.val)
71#                 dfs_graph_builder(node.left, node)
72                
73#             # Connect current node to right child
74#             if node.right:
75#                 graph[node.val].append(node.right.val)
76#                 dfs_graph_builder(node.right, node)     
77        
78#         dfs_graph_builder(root, None)
79
80#         if target.val not in graph:
81#             return []
82
83#         dist_so_far = 0
84#         dq = deque([target.val])
85#         visited = {target.val}
86
87#         # BFS to find the k-th level neighbors
88#         while dq:
89#             # Increment distance AFTER processing the previous level
90#             for _ in range(len(dq)):
91#                 node = dq.popleft()
92                
93#                 for neighbor in graph[node]:
94#                     if neighbor not in visited:
95#                         visited.add(neighbor)
96#                         dq.append(neighbor)
97            
98#             dist_so_far += 1
99#             # Check if the level we just finished adding to dq is level K
100#             if dist_so_far == k:
101#                 return list(dq)
102        
103#         return []