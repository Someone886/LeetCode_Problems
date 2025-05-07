# Last updated: 5/6/2025, 11:46:47 PM
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = {}
        n, m = len(obstacleGrid), len(obstacleGrid[0])

        def helper(r, c):
            if r < 0 or r >= n or c < 0 or c >= m:
                return 0
            
            if obstacleGrid[r][c] == 1:
                return 0
            
            if r == (n - 1) and c == (m - 1):
                return 1
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            ways = helper(r + 1, c) + helper(r, c + 1)
            dp[(r, c)] = ways

            return ways
        
        ans = helper(0, 0)
        return ans