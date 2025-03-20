# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        
        if root == None:
            return str(ans)
        
        curr_level = [root]
        while len(curr_level) != 0:
            next_level = []
            
            for _ in range(len(curr_level)):
                node = curr_level.pop(0)
                
                if node != None:
                    ans.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
                else:
                    ans.append(None)
                    
            curr_level = next_level
        
        # print(str(ans))
        return str(ans)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = eval(data)
        
        if len(data) == 0:
            return None
        
        root = TreeNode(data.pop(0))
        curr_level = [root]
        
        while len(curr_level) != 0:
            next_level = []
            
            for _ in range(len(curr_level)):
                node = curr_level.pop(0)
                
                next_left_val = data.pop(0)
                if next_left_val != None:
                    node.left = TreeNode(next_left_val)
                    next_level.append(node.left)
                
                next_right_val = data.pop(0)
                if next_right_val != None:
                    node.right = TreeNode(next_right_val)
                    next_level.append(node.right)
            
            curr_level = next_level
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))