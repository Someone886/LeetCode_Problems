# Last updated: 4/10/2025, 1:26:36 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node == None:
                return [True, 0]
            
            left, right = dfs(node.left), dfs(node.right)
            balanced = True
            if left[0] == False or right[0] == False:
                balanced = False
            if abs(left[1] - right[1]) > 1:
                balanced = False
        
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]