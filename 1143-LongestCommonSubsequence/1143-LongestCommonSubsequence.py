# Last updated: 4/16/2025, 6:16:51 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0
        
        n = len(prices)
        dp = [-1] * n

        def helper(buy_day):
            if buy_day >= n:
                return 0
            
            if dp[buy_day] != -1:
                return dp[buy_day]
            
            cost = -prices[buy_day]
            profit = 0
            for i in range(buy_day + 1, n):
                profit = max(profit, cost + prices[i] + helper(i + 2))
            
            profit = max(profit, helper(buy_day + 1))
            
            dp[buy_day] = profit
            return dp[buy_day]
        
        return helper(0)