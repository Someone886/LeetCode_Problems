# Last updated: 4/10/2025, 2:49:49 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        this_layer = [root]
        ans = []

        while this_layer:
            ans.append([node.val for node in this_layer])
            next_layer = []

            for node in this_layer:
                if node.left != None:
                    next_layer.append(node.left)
                if node.right != None:
                    next_layer.append(node.right)
            
            this_layer = next_layer
        
        return ans