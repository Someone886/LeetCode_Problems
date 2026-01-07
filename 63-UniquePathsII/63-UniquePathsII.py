# Last updated: 1/6/2026, 8:54:31 PM
1class Solution:
2    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
3        # Memoization table to store number of ways to reach end from (r, c)
4        memo = {}
5        m, n = len(obstacleGrid), len(obstacleGrid[0])
6        
7        # Directions: Right and Down only (no need to visit back up or left)
8        directions = [(0, 1), (1, 0)]
9
10        def dfs(r, c):
11            # 1. Base Case: Out of bounds
12            if not (0 <= r < m and 0 <= c < n):
13                return 0
14            
15            # 2. Base Case: Obstacle encountered
16            if obstacleGrid[r][c] == 1:
17                return 0
18            
19            # 3. Base Case: Reached the destination (bottom-right)
20            if r == m - 1 and c == n - 1:
21                return 1
22            
23            # 4. Check memo: Return result if already calculated
24            if (r, c) in memo:
25                return memo[(r, c)]
26            
27            # 5. Recursive step: Sum paths from going Right and Down
28            total_paths = 0
29            for dr, dc in directions:
30                total_paths += dfs(r + dr, c + dc)
31            
32            # 6. Store in memo and return
33            memo[(r, c)] = total_paths
34            return total_paths
35        
36        # Start the recursive search from the top-left corner
37        return dfs(0, 0)