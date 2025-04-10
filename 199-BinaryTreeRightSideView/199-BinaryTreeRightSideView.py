# Last updated: 4/10/2025, 3:06:46 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        view = []
        q = deque()
        q.append(root)

        while q:
            q_len = len(q)
            node = None

            for i in range(q_len):
                node = q.popleft()
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)

            view.append(node.val)
        
        return view