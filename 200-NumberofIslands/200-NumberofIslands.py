class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def visit_next(r, c, grid):
            if r < 0 or r > m - 1 or c < 0 or c > n - 1:
                return

            if grid[r][c] == "0":
                return

            grid[r][c] = "0"

            visit_next(r - 1, c, grid)
            visit_next(r + 1, c, grid)
            visit_next(r, c - 1, grid)
            visit_next(r, c + 1, grid)
        
        num = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    num += 1
                    visit_next(r, c, grid)
        
        return num