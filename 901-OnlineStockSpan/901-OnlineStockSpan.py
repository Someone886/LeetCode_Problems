# Last updated: 1/11/2026, 5:56:42 PM
1class Solution:
2    def maxWidthRamp(self, nums: List[int]) -> int:
3        n = len(nums)
4        max_right = [0] * n
5        max_right[-1] = nums[-1]
6        
7        # Precompute suffix maximums
8        for i in range(n - 2, -1, -1):
9            max_right[i] = max(nums[i], max_right[i+1])
10        
11        L = 0
12        max_length = 0
13
14        # R expands greedily
15        for R in range(n):
16            # L only moves forward if the current nums[L] is too big 
17            # to form a ramp with ANY remaining element to the right.
18            while nums[L] > max_right[R]:
19                L += 1
20            
21            # Since the while loop ensures nums[L] <= max_right[R],
22            # every (L, R) pair here is a valid candidate for the max width.
23            max_length = max(max_length, R - L)
24        
25        return max_length
26
27'''
28Using monotonicly decreasing stack + greedy: first pass finds possible starting indexes, second pass finds possible ending indexes.
29
30class Solution:
31    def maxWidthRamp(self, nums: List[int]) -> int:
32        n = len(nums)
33        stack = []
34        
35        # Phase 1: Build a monotonic decreasing stack of indices
36        for i in range(n):
37            if not stack or nums[i] < nums[stack[-1]]:
38                stack.append(i)
39        
40        max_width = 0
41        
42        # Phase 2: Traverse from right to left to find the widest ramp
43        for j in range(n - 1, -1, -1):
44            # While the current number can form a ramp with the index at stack top
45            while stack and nums[j] >= nums[stack[-1]]:
46                # Calculate width and update max_width
47                start_index = stack.pop()
48                max_width = max(max_width, j - start_index)
49                
50        return max_width
51'''