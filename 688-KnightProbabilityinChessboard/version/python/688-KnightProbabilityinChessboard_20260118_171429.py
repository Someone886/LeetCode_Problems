# Last updated: 1/18/2026, 5:14:29 PM
1class Solution:
2    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
3        # Your DP dictionary to store (r, c, moves_left)
4        memo = {}
5        
6        # Possible knight moves
7        directions = [
8            (1, 2), (1, -2), (-1, 2), (-1, -2),
9            (2, 1), (2, -1), (-2, 1), (-2, -1)
10        ]
11
12        def dfs(r, c, k_left):
13            # Base Case 1: Off the board
14            if not (0 <= r < n and 0 <= c < n):
15                return 0
16            
17            # Base Case 2: No moves left (and still on the board)
18            if k_left == 0:
19                return 1
20            
21            # Check DP cache
22            state = (r, c, k_left)
23            if state in memo:
24                return memo[state]
25            
26            total_prob = 0
27            # Try all 8 moves
28            for dr, dc in directions:
29                # Each move has a 1/8 chance of being chosen
30                total_prob += dfs(r + dr, c + dc, k_left - 1) / 8.0
31            
32            # Save to dictionary
33            memo[state] = total_prob
34            return total_prob
35
36        return dfs(row, column, k)