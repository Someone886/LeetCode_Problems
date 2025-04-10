# Last updated: 4/10/2025, 1:40:46 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if node == None:
                return 'N'
            return f"({node.val}, {serialize(node.left)}, {serialize(node.right)})"
        
        serialized_root = serialize(root)
        serialized_subroot = serialize(subRoot)
        return serialized_subroot in serialized_root