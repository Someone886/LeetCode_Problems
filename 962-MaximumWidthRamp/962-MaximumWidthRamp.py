# Last updated: 1/11/2026, 5:43:49 PM
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