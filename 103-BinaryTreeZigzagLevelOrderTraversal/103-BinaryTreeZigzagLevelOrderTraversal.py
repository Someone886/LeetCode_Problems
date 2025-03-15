# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        ans = []
        
        this_level = [root]
        next_level = []

        even_level = False
        
        while len(this_level) != 0:
            this_level_values = []
            
            for node in this_level:
                this_level_values.append(node.val)

                if node.left != None:
                    next_level.append(node.left)
                if node.right != None:
                    next_level.append(node.right)
                
            this_level = next_level
            next_level = []
            
            if even_level:
                ans.append(this_level_values[::-1])
            else:
                ans.append(this_level_values)
            
            even_level = not even_level
        
        return ans