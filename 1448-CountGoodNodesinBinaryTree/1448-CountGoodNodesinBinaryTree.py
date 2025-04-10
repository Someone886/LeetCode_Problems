# Last updated: 4/10/2025, 3:19:14 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        cnt = 0

        def counter(node, max_val):
            nonlocal cnt

            if node == None:
                return
            
            new_max = max_val
            if node.val >= max_val:
                new_max = node.val
                cnt += 1
            
            counter(node.left, new_max)
            counter(node.right, new_max)
        
        counter(root, root.val)
        return cnt