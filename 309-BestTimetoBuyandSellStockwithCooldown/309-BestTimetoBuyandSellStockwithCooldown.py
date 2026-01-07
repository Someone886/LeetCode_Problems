# Last updated: 1/6/2026, 11:01:08 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        # dp stores the maximum profit possible from (day_index, has_stock)
4        dp = {}
5        n = len(prices)
6
7        def helper(day_index, has_stock):
8            # Base Case 1: If we go past the last day, no more profit can be made.
9            # This handles the day_index + 2 skip after a sale.
10            if day_index >= n:
11                return 0
12            
13            # Base Case 2: Last day optimization.
14            # If we have stock, sell it; otherwise, we can't do anything.
15            if day_index == n - 1:
16                return prices[day_index] if has_stock else 0
17            
18            # Check memoization table to avoid recalculating the same state.
19            if (day_index, has_stock) in dp:
20                return dp[(day_index, has_stock)]
21            
22            if has_stock:
23                # We currently own a stock. We have two choices:
24                # 1. SELL: Gain current price and skip 1 day (move to day + 2).
25                # 2. HOLD: Do nothing today and move to the next day.
26                sell = prices[day_index] + helper(day_index + 2, False)
27                hold = helper(day_index + 1, True)
28                dp[(day_index, has_stock)] = max(sell, hold)
29            else:
30                # We do not own a stock. We have two choices:
31                # 1. BUY: Spend current price (negative profit) and move to next day.
32                # 2. REST: Do nothing today and move to the next day.
33                buy = -prices[day_index] + helper(day_index + 1, True)
34                rest = helper(day_index + 1, False)
35                dp[(day_index, has_stock)] = max(buy, rest)
36            
37            return dp[(day_index, has_stock)]
38        
39        # Start at day 0 without any stock.
40        return helper(0, False)