# Last updated: 4/10/2025, 1:36:39 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same_sub_tree(container_node, target_node):
            if not target_node and not container_node:
                return True
        
            if (not container_node and target_node) or (container_node and not target_node):
                return False
            
            if container_node.val != target_node.val:
                return False
            
            return same_sub_tree(container_node.left, target_node.left) and \
                    same_sub_tree(container_node.right, target_node.right)
        
        def dfs(node):
            if node == None:
                return False
            
            if same_sub_tree(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)