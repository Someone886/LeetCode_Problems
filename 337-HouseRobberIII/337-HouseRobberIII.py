# Last updated: 4/30/2025, 11:56:41 PM
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

            robIt = root.val 
            robIt += (l[1] + r[1])
            #if you are going to take the node , then skip its child with exclusion

            skip = max(l) + max(r)
            #since this node was skiped , you can pick child or skip child

            return robIt, skip
        return max(solve(root))






        
        return solve(root)
