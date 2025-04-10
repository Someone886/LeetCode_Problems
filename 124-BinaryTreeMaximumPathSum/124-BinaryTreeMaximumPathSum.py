# Last updated: 4/10/2025, 5:09:38 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = None

        def helper(node):
            nonlocal max_sum

            if node == None:
                return 0
            
            left_sum = helper(node.left)
            right_sum = helper(node.right)

            left_max = max(0, left_sum)
            right_max = max(0, right_sum)

            node_max = node.val + left_max + right_max
            if max_sum == None:
                max_sum = node_max
            elif node_max > max_sum:
                max_sum = node_max
            
            return max(0, node.val + max(left_sum, right_sum))
        
        helper(root)
        return max_sum