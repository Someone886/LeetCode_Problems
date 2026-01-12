# Last updated: 1/11/2026, 10:56:11 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def goodNodes(self, root: TreeNode) -> int:
10        good_nodes_cnt = 0
11
12        def dfs(node, max_so_far):
13            nonlocal good_nodes_cnt
14
15            if node.val >= max_so_far:
16                good_nodes_cnt += 1
17            
18            new_max_so_far = max(node.val, max_so_far)
19            if node.left:
20                dfs(node.left, new_max_so_far)
21            if node.right:
22                dfs(node.right, new_max_so_far)
23            
24        dfs(root, float("-inf"))
25        return good_nodes_cnt
26            