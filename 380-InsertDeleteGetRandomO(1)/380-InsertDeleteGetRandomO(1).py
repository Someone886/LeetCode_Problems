// Last updated: 3/20/2025, 10:03:17 PM
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

        if root == None:
            return "None"
        
        ans = []
        q = deque()
        q.append(root)
        
        while len(q) != 0:
            node = q.popleft()
            if node != None:
                ans.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                ans.append("None")
        
        return ','.join(ans)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if data == "None":
            return None

        data = deque(map(lambda x: None if x == "None" else int(x), data.split(",")))

        root = TreeNode(data.popleft())
        q = deque([root])
        
        while len(q) != 0:
            node = q.popleft()

            if node != None:
                left = data.popleft()
                if left != None:
                    left_node = TreeNode(left)
                    node.left = left_node
                    q.append(left_node)
                
                right = data.popleft()
                if right != None:
                    right_node = TreeNode(right)
                    node.right = right_node
                    q.append(right_node)
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))