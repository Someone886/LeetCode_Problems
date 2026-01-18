# Last updated: 1/18/2026, 4:40:24 PM
1class Solution:
2    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
3        dp = {}
4        MOD = 10**9 + 7
5
6        def dfs(n_left, target_left):
7            if target_left == 0 and n_left == 0:
8                return 1
9            
10            if target_left < 0 or n_left < 0:
11                return 0
12            
13            # Pruning: improved from 30% to 80% lol
14            if target_left < n_left or target_left > n_left * k:
15                return 0
16            
17            if (n_left, target_left) in dp:
18                return dp[(n_left, target_left)]
19            
20            total_ways = 0
21            
22            for i in range(1, k + 1):
23                total_ways += dfs(n_left - 1, target_left - i) % MOD
24            
25            dp[(n_left, target_left)] = total_ways % MOD
26            return dp[(n_left, target_left)]
27        
28        return dfs(n, target) % MOD