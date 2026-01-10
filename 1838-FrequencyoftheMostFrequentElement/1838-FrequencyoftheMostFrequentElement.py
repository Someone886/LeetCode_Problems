# Last updated: 1/10/2026, 4:53:55 PM
1class Solution:
2    def maxFrequency(self, nums: list[int], k: int) -> int:
3        # Sort so we can greedily increment smaller numbers to match 
4        # the current largest number in the window (nums[R])
5        nums.sort()
6
7        L = 0
8        R = 1
9        # Initial window [L] starts with just the first element
10        total_sum = nums[L] 
11        max_freq_cnt = 1
12        n = len(nums)
13
14        while R < n:
15            # Expand window by including the next largest candidate
16            total_sum += nums[R]
17
18            # VALIDATION LOGIC:
19            # nums[R] * (R - L + 1) is the "target sum" if all elements in window were nums[R].
20            # total_sum + k is the "budget sum" (current values + maximum allowed increments).
21            # If target > budget, the window is too wide for our budget k.
22            while nums[R] * (R - L + 1) > total_sum + k:
23                # Shrink from the left to reduce the "target sum" requirements
24                total_sum -= nums[L]
25                L += 1
26            
27            # Record the largest valid window size found so far
28            max_freq_cnt = max(max_freq_cnt, R - L + 1)
29            
30            # Move to the next potential maximum value
31            R += 1
32        
33        return max_freq_cnt