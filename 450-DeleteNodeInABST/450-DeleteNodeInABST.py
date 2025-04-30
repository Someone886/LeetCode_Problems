# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # 1) Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        # 2) root.val == key ⇒ delete this node
        # Case A: only one child (or none)
        if not root.left:
            return root.right

        if not root.right:
            return root.left

        # Case B: two children → replace root with the deepest left node of root's right node (min of the root's right)
        successor, successor_parent = self._getMin(root.right)
        root.val = successor.val

        # delete that successor node from the right subtree
        if successor_parent != None:
            successor_parent.left = successor.right
        else:
            # means root.right has no left node
            root.right = successor.right
        
        return root

    def _getMin(self, node: TreeNode):
        """Return the node with minimum value in this subtree, and the parent of this node."""
        prev = None

        while node.left:
            prev = node
            node = node.left
        
        return node, prev

'''
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        
        dummy_node = TreeNode(0, left = root)
        
        def explore(node, last_node, dir):
            if node == None:
                return
            
            if node.val < key:
                explore(node.right, node, "r")
            
            elif node.val > key:
                explore(node.left, node, "l")
            
            else:
                l, r = node.left, node.right
                if not l and not r:
                    if dir == "l":
                        last_node.left = None
                    else:
                        last_node.right = None
                elif not l:
                    if dir == "l":
                        last_node.left = r
                    else:
                        last_node.right = r
                elif not r:
                    if dir == "l":
                        last_node.left = l
                    else:
                        last_node.right = l
                else:
                    curr = r
                    while curr.left != None:
                        curr = curr.left
                    curr.left = l

                    if dir == "l":
                        last_node.left = r
                    else:
                        last_node.right = r
        
        explore(root, dummy_node, 'l')
        return dummy_node.left
'''