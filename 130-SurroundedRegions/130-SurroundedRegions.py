# Last updated: 4/14/2025, 11:27:40 PM
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        q = deque()

        def visit(r, c):
            if r < 0 or r >= n or c < 0 or c >= m:
                return
            
            if board[r][c] == "X" or board[r][c] == "#":
                return
            
            if board[r][c] == "O":
                board[r][c] = "#"

            q.append((r, c))
        
        for r in range(n):
            if board[r][0] == "O":
                visit(r, 0)
            if board[r][m-1] == "O":
                visit(r, m-1)
        
        for c in range(m):
            if board[0][c] == "O":
                visit(0, c)
            if board[n-1][c] == "O":
                visit(n-1, c)
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                visit(r + 1, c)
                visit(r - 1, c)
                visit(r, c + 1)
                visit(r, c - 1)
        
        for r in range(n):
            for c in range(m):
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"