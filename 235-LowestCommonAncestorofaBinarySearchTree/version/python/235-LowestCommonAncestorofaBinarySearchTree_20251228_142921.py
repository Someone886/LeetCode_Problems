# Last updated: 12/28/2025, 2:29:21 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        if not root or not p or not q:
11            return None
12        
13        # if both p and q are to the left of root
14        if (max(p.val, q.val)) < root.val:
15            return self.lowestCommonAncestor(root.left, p, q)
16        
17        # if both p and q are to the right of root
18        elif (min(p.val, q.val)) > root.val:
19            return self.lowestCommonAncestor(root.right, p, q)
20        
21        # if p and q on two sides, then root is the LCA
22        else:
23            return root