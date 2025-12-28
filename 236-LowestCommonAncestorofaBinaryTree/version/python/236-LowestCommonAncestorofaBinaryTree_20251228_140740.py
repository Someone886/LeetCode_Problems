# Last updated: 12/28/2025, 2:07:40 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        # Base case: if we hit a null node
11        if not root:
12            return None
13        
14        # Base case 2: if root contains p or q:
15        if root == p or root == q:
16            return root
17        
18        # Look for p and q in the left and right subtrees
19        # If left or right is not None, then left or right contains p or q or both
20        left = self.lowestCommonAncestor(root.left, p, q)
21        right = self.lowestCommonAncestor(root.right, p, q)
22        
23        # 1. If both 'left' and 'right' contains p or q, then current node is the LCA
24        if left and right:
25            return root
26        
27        # 2. Otherwise, the not None child contains both p and q
28        return left if left else right