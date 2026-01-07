# Last updated: 1/7/2026, 1:00:30 AM
1class Solution:
2    def cherryPickup(self, grid: List[List[int]]) -> int:
3        ROWS, COLS = len(grid), len(grid[0])
4        dp = {}
5
6        def dfs(r, c1, c2):
7            # 1. Boundary Check: If robots go off the grid
8            if c1 < 0 or c1 >= COLS or c2 < 0 or c2 >= COLS:
9                return float('-inf')
10
11            # 2. Check Memoization
12            if (r, c1, c2) in dp:
13                return dp[(r, c1, c2)]
14
15            # 3. Collect Cherries:
16            # If robots are in the same cell, they only pick it up ONCE.
17            cherries = grid[r][c1]
18            if c1 != c2:
19                cherries += grid[r][c2]
20
21            # 4. Base Case: Reached the bottom row
22            if r == ROWS - 1:
23                return cherries
24            
25            # 5. Recursive Step: 
26            # Both robots move simultaneously to 3 possible next columns (-1, 0, 1).
27            # This creates 3 * 3 = 9 possible next states.
28            max_future = 0
29            for c1_d in [-1, 0, 1]:
30                for c2_d in [-1, 0, 1]:
31                    max_future = max(max_future, dfs(r + 1, c1 + c1_d, c2 + c2_d))
32            
33            # Result for current state is cherries today + best possible cherries tomorrow
34            res = cherries + max_future
35            dp[(r, c1, c2)] = res
36            return res
37        
38        # Start Robot 1 at top-left and Robot 2 at top-right
39        return dfs(0, 0, COLS - 1)