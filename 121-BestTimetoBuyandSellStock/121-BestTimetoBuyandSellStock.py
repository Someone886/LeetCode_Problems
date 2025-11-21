# Last updated: 11/21/2025, 8:53:50 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0

        for curr_price in prices[1:]:
            if curr_price < min_price:
                min_price = curr_price
            elif curr_price - min_price > profit:
                profit = curr_price - min_price

        return profit


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         max_after = [0] * n
#         max_profit = 0

#         for i in range(n-2, -1, -1):
#             max_after_i = max(prices[i + 1], max_after[i + 1])
#             max_after[i] = max_after_i

#             profit = max_after_i - prices[i]
#             if profit > max_profit:
#                 max_profit = profit
        
#         return max_profit
