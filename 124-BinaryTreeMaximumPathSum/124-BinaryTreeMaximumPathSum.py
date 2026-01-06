# Last updated: 1/5/2026, 11:20:26 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def maxPathSum(self, root: Optional[TreeNode]) -> int:
10        # Initialize with a very small number to handle all-negative trees
11        self.global_max = float('-inf')
12
13        def get_gain(node):
14            if not node:
15                return 0
16
17            # 1. Recursively get the max gain from left and right subtrees.
18            # If the gain is negative, we treat it as 0 (we ignore that branch).
19            left_gain = max(get_gain(node.left), 0)
20            right_gain = max(get_gain(node.right), 0)
21
22            # 2. Calculate the price of a path peaking at the current node.
23            # This is the "Full Path" (Left + Root + Right)
24            current_path_sum = node.val + left_gain + right_gain
25
26            # 3. Update the global maximum if the current path is better.
27            self.global_max = max(self.global_max, current_path_sum)
28
29            # 4. Return the "Max Gain" to the parent.
30            # A path can only use ONE branch to continue upward.
31            return node.val + max(left_gain, right_gain)
32
33        get_gain(root)
34        return self.global_max