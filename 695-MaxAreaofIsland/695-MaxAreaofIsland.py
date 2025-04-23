class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        n = len(grid)
        m = len(grid[0])

        def visit(r, c):
            if r < 0 or r >= n or c < 0 or c >= m:
                return 0
            
            if grid[r][c] == 0 or grid[r][c] == -1:
                return 0
            
            grid[r][c] = -1
            return 1 + visit(r + 1, c) + \
                        visit(r - 1, c) + \
                        visit(r, c + 1) + \
                        visit(r, c - 1)

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    curr_area = visit(r, c)
                    if curr_area > max_area:
                        max_area = curr_area
        
        return max_area
        