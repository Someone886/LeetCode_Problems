# Last updated: 5/18/2025, 1:57:01 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node):
            if node == None:
                return
            
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ans