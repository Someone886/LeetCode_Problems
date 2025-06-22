# Last updated: 6/22/2025, 2:51:28 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if root is None:
                return (0,0)

            l = solve(root.left)
            r = solve(root.right)

            # if robbed this node, must skip the next child by selecting index 1
            rob_this = root.val + (l[1] + r[1]) 

            skip_this = max(l) + max(r)

            return rob_this, skip_this

        return max(solve(root))

'''
# Pure DP but not optimal:

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        
        def max_node(node, robbed_last):
            if not node:
                return 0
            
            if (node, robbed_last) in dp:
                return dp[(node, robbed_last)]

            if robbed_last:
                max_left = max_node(node.left, False)
                max_right = max_node(node.right, False)
                dp[(node, robbed_last)] = max_left + max_right
                return dp[(node, robbed_last)]

            else:
                rob_this = node.val + max_node(node.left, True) + max_node(node.right, True)
                not_rob_this = max_node(node.left, False) + max_node(node.right, False)
                dp[(node, robbed_last)] = max(rob_this, not_rob_this)
                return dp[(node, robbed_last)]
        
        ans = max_node(root, False)
        return ans
'''