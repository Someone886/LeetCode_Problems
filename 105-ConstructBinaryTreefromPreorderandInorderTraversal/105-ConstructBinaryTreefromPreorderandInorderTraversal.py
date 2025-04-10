# Last updated: 4/10/2025, 4:30:12 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        index_root_val_inorder = inorder.index(root_val)
        
        root.left = self.buildTree(preorder[1:1 + index_root_val_inorder], inorder[:index_root_val_inorder])
        root.right = self.buildTree(preorder[1 + index_root_val_inorder:], inorder[index_root_val_inorder + 1:])
        
        return root
    