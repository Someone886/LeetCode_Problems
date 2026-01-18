# Last updated: 1/18/2026, 4:32:52 PM
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
13            if (n_left, target_left) in dp:
14                return dp[(n_left, target_left)]
15            
16            total_ways = 0
17            
18            for i in range(1, k + 1):
19                total_ways += dfs(n_left - 1, target_left - i) % MOD
20            
21            dp[(n_left, target_left)] = total_ways
22            return dp[(n_left, target_left)]
23        
24        return dfs(n, target) % (10**9 + 7)