# Last updated: 1/6/2026, 11:23:00 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        # We track four states. 'inf' ensures the first price we see 
4        # always updates the 'min' variables.
5        min_sf1 = float("inf")  # Best price to buy for Transaction 1
6        min_sf2 = float("inf")  # Best "Effective Cost" to buy for Transaction 2
7        max_p1 = 0              # Best profit after Transaction 1
8        max_p2 = 0              # Best total profit after Transaction 2
9        
10        for p in prices:
11            # --- TRANSACTION 1 ---
12            # Logic: Find the lowest price seen so far to start our first trade.
13            min_sf1 = min(min_sf1, p)
14            
15            # Logic: If we sold today, is the profit (Price - MinCost) 
16            # better than our previous best first profit?
17            max_p1 = max(max_p1, p - min_sf1)
18            
19            # --- TRANSACTION 2 ---
20            # Logic (The Reinvestment Trick): 
21            # We treat the profit from max_p1 as a discount. 
22            # If we buy a second stock at price 'p', our "Net Cost" 
23            # is (Price - Previous Profit). We want to minimize this.
24            min_sf2 = min(min_sf2, p - max_p1)
25            
26            # Logic: The final total profit. 
27            # (Current Price - Effective Cost).
28            # This is mathematically equivalent to: 
29            # (Current Price - p_second_buy) + Profit_from_trade_1
30            max_p2 = max(max_p2, p - min_sf2)
31            
32        return max_p2
33
34# DP
35# class Solution:
36#     def maxProfit(self, prices: List[int]) -> int:
37#         dp = {}
38#         n = len(prices)
39
40#         def dfs(day_index, has_stock, transaction_cnt):
41#             if transaction_cnt >= 2:
42#                 return 0
43            
44#             if day_index == n - 1:
45#                 if not has_stock:
46#                     return 0
47#                 else:
48#                     return prices[n - 1]
49            
50#             if (day_index, has_stock, transaction_cnt) in dp:
51#                 return dp[(day_index, has_stock, transaction_cnt)]
52
53#             if has_stock:
54#                 # Option 1: Sell today (consumes 1 transaction)
55#                 # Option 2: Keep holding
56#                 res = max(prices[day_index] + \
57#                             dfs(day_index + 1, False, transaction_cnt + 1),
58#                           dfs(day_index + 1, True, transaction_cnt))
59#             else:
60#                 # Option 1: Buy today
61#                 # Option 2: Stay empty
62#                 res = max(-prices[day_index] + \
63#                             dfs(day_index + 1, True, transaction_cnt),
64#                           dfs(day_index + 1, False, transaction_cnt))
65            
66#             dp[(day_index, has_stock, transaction_cnt)] = res
67#             return res
68        
69#         return dfs(0, False, 0)