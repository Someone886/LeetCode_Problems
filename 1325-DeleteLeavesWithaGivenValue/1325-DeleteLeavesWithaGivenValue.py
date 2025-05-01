# Last updated: 5/1/2025, 1:03:30 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if node.left:
                dfs(node.left)
                if node.left.val == 0:
                    node.left = None
            
            if node.right:
                dfs(node.right)
                if node.right.val == 0:
                    node.right = None
            
            if node.left == None and node.right == None:
                if node.val == target:
                    node.val = 0
        
        dfs(root)
        if root.val == 0:
            return None
        else:
            return root