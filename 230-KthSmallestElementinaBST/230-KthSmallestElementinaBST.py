# Last updated: 4/10/2025, 2:54:41 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root == None:
            return None
        
        ans = -1
        cnt = 0

        def in_order(node):
            nonlocal ans, cnt

            if node == None:
                return
            
            in_order(node.left)
            
            cnt += 1
            if cnt == k:
                ans = node.val
            
            in_order(node.right)
        
        in_order(root)
        return ans