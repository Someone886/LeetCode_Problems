# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        ans = []
        root_node = root
        
        def visit_next(node, arr):
            if node.left != None:
                visit_next(node.left, arr)
                
            arr.append(node.val)
            
            if node.right != None:
                visit_next(node.right, arr)
        
        visit_next(root, ans)
        
        return ans