# Last updated: 4/16/2025, 7:22:05 PM
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = {}

        def dfs(index, total):
            if index >= n:
                return 0
            
            if total > amount:
                return 0
            
            if total == amount:
                return 1

            if (index, total) in dp:
                return dp[(index, total)]
            
            dp[(index, total)] = dfs(index, total + coins[index]) + \
                                 dfs(index + 1, total)
            
            return dp[(index, total)]
        
        ans = dfs(0, 0)
        return ans