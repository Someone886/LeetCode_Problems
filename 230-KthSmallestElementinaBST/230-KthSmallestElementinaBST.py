# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k_left = k
        self.val = 0

        def dfs(node):
            if node.left != None:
                dfs(node.left)
            
            if self.k_left == 1:
                self.val = node.val
            
            self.k_left -= 1

            if self.k_left > 0 and node.right != None:
                dfs(node.right)
        
        dfs(root)
        return self.val
