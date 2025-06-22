# Last updated: 6/22/2025, 2:51:29 PM
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        n = len(matrix)
        m = len(matrix[0])

        def dfs(r, c, prev):
            if r < 0 or r >= n or c < 0 or c >= m:
                return 0
            
            curr = matrix[r][c]
            if curr <= prev:
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            matrix[r][c] = -1

            dp[(r, c)] = 1 + max(dfs(r + 1, c, curr),\
                                 dfs(r - 1, c, curr),\
                                 dfs(r, c + 1, curr),\
                                 dfs(r, c - 1, curr))
            
            matrix[r][c] = curr
            return dp[(r, c)]
        
        max_length = 1

        for i in range(n):
            for j in range(m):
                length = dfs(i, j, -1)
                max_length = length if length > max_length else max_length
        
        return max_length