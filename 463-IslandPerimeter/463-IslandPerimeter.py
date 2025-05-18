# Last updated: 5/18/2025, 12:56:09 AM
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        # If the next cell is out of boundary or water, then increase the perimeter by 1.
        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m:
                return 1
            
            if grid[r][c] == 0:
                return 1
            
            if grid[r][c] == -1:
                return 0
            
            grid[r][c] = -1
            
            parimeter = dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

            return parimeter
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    parimeter = dfs(r, c)
                    return parimeter