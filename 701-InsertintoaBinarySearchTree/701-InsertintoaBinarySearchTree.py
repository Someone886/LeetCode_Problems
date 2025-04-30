# Last updated: 4/29/2025, 10:12:28 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        def explore(node):
            node_val = node.val
            if val < node.val:
                if node.left == None:
                    node.left = TreeNode(val)
                else:
                    explore(node.left)
            else:
                if node.right == None:
                    node.right = TreeNode(val)
                else:
                    explore(node.right)
        
        explore(root)
        return root