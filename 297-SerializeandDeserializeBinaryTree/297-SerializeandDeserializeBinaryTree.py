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
        
        q = [root]
        
        while len(q) != 0:
            node = q.pop(0)
            if node != None:
                ans.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                ans.append(None)
        
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
        q = [root]
        
        while len(q) != 0:
            node = q.pop(0)

            if node != None:
                left = data.pop(0)
                if left != None:
                    left_node = TreeNode(left)
                    node.left = left_node
                    q.append(left_node)
                
                right = data.pop(0)
                if right != None:
                    right_node = TreeNode(right)
                    node.right = right_node
                    q.append(right_node)
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))