# Last updated: 4/16/2025, 6:37:56 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        # state: buy or sell
        # if buy, move time to i+1
        # if sell, move time to i+2

        dp = {} # key = (i, can_buy), val = max_profit

        def dfs(i, can_buy):
            if i >= len(prices):
                return 0
            
            if (i, can_buy) in dp:
                return dp[(i, can_buy)]
            
            if can_buy:
                buy = -prices[i] + dfs(i + 1, False)
                cooldown = dfs(i + 1, True)
                dp[(i, can_buy)] = max(buy, cooldown)
            else:
                sell = prices[i] + dfs(i + 2, True)
                cooldown = dfs(i + 1, False)
                dp[(i, can_buy)] = max(sell, cooldown)
            
            return dp[(i, can_buy)]
        
        return dfs(0, True)
        