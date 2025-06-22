# Last updated: 6/22/2025, 2:52:35 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        max_depth = [0]

        def helper(node, depth):
            if node == None:
                if depth > max_depth[0]:
                    max_depth[0] = depth
                return
            
            helper(node.left, depth + 1)
            helper(node.right, depth + 1)
        
        helper(root, 0)

        return max_depth[0]