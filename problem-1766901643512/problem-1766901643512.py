# Last updated: 12/28/2025, 1:00:43 AM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        so_far = []
4        r, c = len(board), len(board[0])
5        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
6
7        def search(x, y):
8            if board[x][y] != word[len(so_far)]:
9                return
10            
11            so_far.append(board[x][y])
12
13            if len(so_far) == len(word):
14                return True
15            
16            temp = board[x][y]
17            board[x][y] = "-1"
18
19            for dx, dy in directions:
20                if 0 <= x + dx < r and 0 <= y + dy < c:
21                    ans = search(x+dx, y+dy)
22                    if ans:
23                        board[x][y] = temp
24                        return True
25            
26            board[x][y] = temp
27            so_far.pop()
28            
29            return False
30        
31        for i in range(r):
32            for j in range(c):
33                if search(i, j):
34                    return True
35        
36        return False