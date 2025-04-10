# Last updated: 4/10/2025, 1:11:10 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        res = True

        def max_length(node, depth):
            nonlocal res

            if node == None:
                return depth
            
            left_max = max_length(node.left, depth)
            right_max = max_length(node.right, depth)

            if left_max > right_max + 1 or right_max > left_max + 1:
                res = False
            
            return 1 + max(left_max, right_max)
        
        max_length(root, 0)
        return res