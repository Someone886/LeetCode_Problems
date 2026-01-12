# Last updated: 1/11/2026, 7:15:54 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
10        dq = deque()
11        dq.append(root)
12        curr_level = 1
13        min_level = 1
14        max_val = root.val
15
16        while dq:
17            curr_val = 0
18
19            for _ in range(len(dq)):
20                node = dq.popleft()
21                curr_val += node.val
22
23                if node.left:
24                    dq.append(node.left)
25                if node.right:
26                    dq.append(node.right)
27                
28            if curr_val > max_val:
29                max_val = curr_val
30                min_level = curr_level
31            
32            curr_level += 1
33        
34        return min_level
35