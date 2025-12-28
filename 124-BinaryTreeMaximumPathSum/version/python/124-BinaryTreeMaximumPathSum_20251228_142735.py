# Last updated: 12/28/2025, 2:27:35 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        max_sum = float("-inf")
10
11        # returns the max child sum PASSING the node
12        def helper(node):
13            nonlocal max_sum
14
15            if node == None:
16                return 0
17            
18            left_sum = helper(node.left)
19            right_sum = helper(node.right)
20
21            left_max = max(0, left_sum)
22            right_max = max(0, right_sum)
23
24            # computes the max path sum PASSING the node
25            node_max = node.val + left_max + right_max
26            if node_max > max_sum:
27                max_sum = node_max
28            
29            # returns the max child sum PASSING the node 
30            return node.val + max(left_max, right_max)
31        
32        helper(root)
33        return max_sum