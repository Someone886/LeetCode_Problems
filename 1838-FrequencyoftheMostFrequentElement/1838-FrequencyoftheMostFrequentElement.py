# Last updated: 1/10/2026, 4:57:20 PM
1from collections import deque
2
3class Solution:
4    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
5        # q will store INDICES of elements in nums.
6        # We maintain it in "monotonically decreasing" order:
7        # nums[q[0]] will always be the largest value in the current window.
8        q = deque() 
9        ans = []
10
11        l = 0
12        for r in range(len(nums)):
13            # MONOTONIC PROPERTY: 
14            # Before adding the current element nums[r], remove all indices from the back
15            # of the queue whose values are smaller than nums[r].
16            # These values will never be the maximum again because nums[r] is larger
17            # and will stay in the window longer.
18            while q and nums[q[-1]] < nums[r]:
19                q.pop()
20            
21            # Add current element's index to the back
22            q.append(r)
23
24            # BOUNDARY CHECK:
25            # If the index at the front of the deque is no longer within the
26            # range [l, r], it means it has "fallen out" of the window.
27            if q[0] < l:
28                q.popleft()
29            
30            # WINDOW COMPLETION:
31            # Once our 'r' pointer has moved at least 'k-1' steps, 
32            # we have a complete window of size k.
33            if r >= k - 1:
34                # The element at the front (q[0]) is the max for the current window.
35                ans.append(nums[q[0]])
36                # Slide the left boundary forward
37                l += 1
38        
39        return ans
40        