# Last updated: 1/11/2026, 7:29:26 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
9        global_max_diff = 0
10
11        def dfs(node):
12            nonlocal global_max_diff
13
14            left_min, left_max = None, None
15            if node.left:
16                left_min, left_max = dfs(node.left)
17            
18            right_min, right_max = None, None
19            if node.right:
20                right_min, right_max = dfs(node.right)
21            
22            min_at_node = max_at_node = node.val
23            if node.left:
24                min_at_node = min(min_at_node, left_min)
25                max_at_node = max(max_at_node, left_max)
26                global_max_diff = max(global_max_diff, abs(node.val - left_min))
27                global_max_diff = max(global_max_diff, abs(node.val - left_max))
28            if node.right:
29                min_at_node = min(min_at_node, right_min)
30                max_at_node = max(max_at_node, right_max)
31                global_max_diff = max(global_max_diff, abs(node.val - right_min))
32                global_max_diff = max(global_max_diff, abs(node.val - right_max))
33            
34            return min_at_node, max_at_node
35        
36        dfs(root)
37        return global_max_diff