# Last updated: 4/26/2025, 10:40:33 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        n = len(prices)

        def helper(day, holding):
            if day >= n:
                return 0

            if (day, holding) in dp:
                return dp[(day, holding)]
            
            if holding:
                profit = max(prices[day] + helper(day + 1, False), helper(day + 1, True))
                dp[(day, holding)] = profit
            else:
                profit = max(-prices[day] + helper(day + 1, True), helper(day + 1, False))
                dp[(day, holding)] = profit
            
            return dp[(day, holding)]
        
        return helper(0, False)