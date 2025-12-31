# Last updated: 12/30/2025, 11:53:32 PM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        # Tracks the cumulative sum as we iterate through the list
4        pre_sum = 0
5        
6        # A hash map to store: {PrefixSumValue : HowManyTimesItOccurred}
7        # We initialize with {0:1} because a sum of 0 has "occurred" once 
8        # (conceptually, before the array starts).
9        dp = {0: 1}
10        
11        # Counter for the total number of valid subarrays
12        ans = 0
13        
14        for num in nums:
15            # 1. Update the running prefix sum
16            pre_sum += num
17            
18            # 2. THE CORE LOGIC:
19            # If (Current Prefix Sum - k) exists in our map, it means 
20            # there is a previous point where the sum was exactly 
21            # (pre_sum - k). The elements between that point and 
22            # the current point MUST sum to k.
23            if pre_sum - k in dp:
24                # Add the number of times that specific previous sum occurred
25                ans += dp[pre_sum - k]
26            
27            # 3. Update the map with the current prefix sum
28            # If it's new, set to 1. If it exists, increment by 1.
29            dp[pre_sum] = 1 + dp.get(pre_sum, 0)
30                
31        return ans