# Last updated: 4/14/2025, 6:58:19 PM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        q = deque()
        good_fruit = 0

        def visit(r, c):
            nonlocal good_fruit
            
            if r < 0 or r >= n or c < 0 or c >= m:
                return
            
            if (r, c) in visited or grid[r][c] == 0:
                return
            
            good_fruit -= 1
            visited.add((r, c))
            q.append([r, c])

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    visited.add((r, c))
                    q.append([r, c])
                elif grid[r][c] == 1:
                    good_fruit += 1
        
        if not q:
            if not good_fruit:
                return 0
            else:
                return -1

        mins = 0
        while q and good_fruit > 0:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                visit(r + 1, c)
                visit(r - 1, c)
                visit(r, c + 1)
                visit(r, c - 1)
            mins += 1
        
        if good_fruit:
            return -1
        
        return mins