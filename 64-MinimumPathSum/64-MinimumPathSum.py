# Last updated: 5/7/2025, 12:02:50 AM
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        # fill from up to down for the first col
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # fill from left to right for the first row
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # fill in the middle cells
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]

'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        n, m = len(grid), len(grid[0])

        def min_sum(r, c):
            if r < 0 or r >= n or c < 0 or c >= m:
                return float('inf')
            
            if r == (n - 1) and c == (m - 1):
                return grid[r][c]
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            local_min = grid[r][c] + min(min_sum(r + 1, c), min_sum(r, c + 1))
            dp[(r, c)] = local_min
            return local_min
        
        ans = min_sum(0, 0)
        return ans
'''