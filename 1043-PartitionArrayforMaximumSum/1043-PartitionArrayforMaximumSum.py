# Last updated: 1/12/2026, 10:31:36 PM
1class Solution:
2    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
3        n = len(arr)
4        dp = {}
5
6        def dfs(index):
7            # Memoization check
8            if index in dp:
9                return dp[index]
10
11            max_at_index = 0
12            current_max_val = 0
13
14            # Try every possible partition size from 1 to k
15            # We must ensure we don't go past the end of the array (min(index + k, n))
16            for i in range(index, min(index + k, n)):
17                current_max_val = max(current_max_val, arr[i])
18                
19                # Partition size is (i - index + 1)
20                # Calculate: (size * max_val_in_partition) + result of the rest of the array
21                partition_sum = (i - index + 1) * current_max_val + dfs(i + 1)
22                
23                max_at_index = max(max_at_index, partition_sum)
24            
25            dp[index] = max_at_index
26            return max_at_index
27        
28        return dfs(0)