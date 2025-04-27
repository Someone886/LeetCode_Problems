# Last updated: 4/26/2025, 10:43:18 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        held_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] >= held_price:
                profit += prices[i] - held_price
                
            held_price = prices[i]
        return profit