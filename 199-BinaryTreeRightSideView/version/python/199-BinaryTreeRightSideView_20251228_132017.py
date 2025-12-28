# Last updated: 12/28/2025, 1:20:17 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
10        if not root:
11            return []
12            
13        dq = deque()
14        dq.append(root)
15        ans = []
16
17        while dq:
18            n = len(dq)
19            for i in range(n):
20                node = dq.popleft()
21                if i == n - 1:
22                    ans.append(node.val)
23
24                if node.left:
25                    dq.append(node.left)
26                if node.right:
27                    dq.append(node.right)
28        
29        return ans