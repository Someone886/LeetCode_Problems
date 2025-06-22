# Last updated: 6/22/2025, 2:51:16 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        res = [0]

        def max_len(node, length):
            if node == None:
                return length
            
            left_max = max_len(node.left, length)
            right_max = max_len(node.right, length)
            
            if left_max + right_max > res[0]:
                res[0] = left_max + right_max

            return 1 + max(left_max, right_max)
        
        max_len(root, 0)
        return res[0]