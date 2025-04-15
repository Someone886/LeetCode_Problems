# Last updated: 4/14/2025, 10:35:31 PM
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        # dp = [[-1] * m for _ in range(n)]
        pac, atl = set(), set()
        INF = 2 ** 32 - 1

        def dfs(r, c, ocean_set, prev_height):
            if r < 0 or c < 0 or r >= n or c >= m or\
             (r, c) in ocean_set or heights[r][c] < prev_height:
             return

            ocean_set.add((r, c))
            dfs(r + 1, c, ocean_set, heights[r][c])
            dfs(r - 1, c, ocean_set, heights[r][c])
            dfs(r, c + 1, ocean_set, heights[r][c])
            dfs(r, c - 1, ocean_set, heights[r][c])

        for c in range(m):
            dfs(0, c, pac, -INF)
            dfs(n - 1, c, atl, -INF)
        
        for r in range(n):
            dfs(r, 0, pac, -INF)
            dfs(r, m - 1, atl, -INF)
        
        ans = []
        for r in range(n):
            for c in range(m):
                if (r, c) in pac and (r, c) in atl:
                    ans.append([r, c])
        
        return ans