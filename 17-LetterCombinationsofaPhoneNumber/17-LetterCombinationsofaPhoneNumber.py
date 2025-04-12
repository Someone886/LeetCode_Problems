# Last updated: 4/12/2025, 1:50:00 AM
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0] * n for _ in range(n)]
        ans = []
        curr = []

        def remove_cells(r, c, board):
            for i in range(n):
                board[r][i] += 1
                board[i][c] += 1
            
            r_copy, c_copy = r - 1, c + 1
            while 0 <= r_copy < n and 0 <= c_copy < n:
                board[r_copy][c_copy] += 1
                r_copy, c_copy = r_copy - 1, c_copy + 1
            
            r_copy, c_copy = r - 1, c - 1
            while 0 <= r_copy < n and 0 <= c_copy < n:
                board[r_copy][c_copy] += 1
                r_copy, c_copy = r_copy - 1, c_copy - 1
            
            r_copy, c_copy = r + 1, c + 1
            while 0 <= r_copy < n and 0 <= c_copy < n:
                board[r_copy][c_copy] += 1
                r_copy, c_copy = r_copy + 1, c_copy + 1
            
            r_copy, c_copy = r + 1, c - 1
            while 0 <= r_copy < n and 0 <= c_copy < n:
                board[r_copy][c_copy] += 1
                r_copy, c_copy = r_copy + 1, c_copy - 1
        
        def release_cells(r, c, board):
            for i in range(n):
                board[r][i] -= 1
                board[i][c] -= 1
            
            r_copy, c_copy = r - 1, c + 1
            while 0 <= r_copy < n and 0 <= c_copy < n:
                board[r_copy][c_copy] -= 1
                r_copy, c_copy = r_copy - 1, c_copy + 1
            
            r_copy, c_copy = r - 1, c - 1
            while 0 <= r_copy < n and 0 <= c_copy < n:
                board[r_copy][c_copy] -= 1
                r_copy, c_copy = r_copy - 1, c_copy - 1
            
            r_copy, c_copy = r + 1, c + 1
            while 0 <= r_copy < n and 0 <= c_copy < n:
                board[r_copy][c_copy] -= 1
                r_copy, c_copy = r_copy + 1, c_copy + 1
            
            r_copy, c_copy = r + 1, c - 1
            while 0 <= r_copy < n and 0 <= c_copy < n:
                board[r_copy][c_copy] -= 1
                r_copy, c_copy = r_copy + 1, c_copy - 1

        def helper(cnt):
            if cnt == n:
                ans.append(curr.copy())
                return
            
            for col in range(n):
                if board[cnt][col] == 0:
                    remove_cells(cnt, col, board)
                    curr.append('.' * col + 'Q' + '.' * (n - 1 - col))

                    helper(cnt + 1)

                    release_cells(cnt, col, board)
                    curr.pop()
        
        helper(0)
        return ans