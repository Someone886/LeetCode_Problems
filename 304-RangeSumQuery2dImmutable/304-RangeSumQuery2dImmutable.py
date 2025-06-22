# Last updated: 6/22/2025, 2:51:33 PM
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = {}
        m, n = len(matrix), len(matrix[0])

        def dfs(r, c):
            if (r, c) in self.dp:
                return self.dp[(r, c)]
            
            if r == 0 and c == 0:
                self.dp[(0, 0)] = matrix[r][c]
                return matrix[r][c]
            
            if r < 0 or c < 0:
                return 0
            
            self.dp[(r, c)] = matrix[r][c] + dfs(r - 1, c) + dfs(r, c - 1) - dfs(r - 1, c - 1)

            return self.dp[(r, c)]
        
        dfs(m - 1, n - 1)
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        def get(r, c):
            # if either index is negative, that prefix is zero
            if r < 0 or c < 0:
                return 0
            return self.dp[(r, c)]
        
        return (get(row2, col2)
                - get(row1 - 1, col2)
                - get(row2, col1 - 1)
                + get(row1 - 1, col1 - 1)
                )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)