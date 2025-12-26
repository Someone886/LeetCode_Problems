# Last updated: 12/26/2025, 6:58:02 PM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        so_far = []
4        r, c = len(board), len(board[0])
5        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
6
7        def search(x, y):
8            temp = board[x][y]
9            so_far.append(board[x][y])
10            board[x][y] = "-1"
11
12            if len(so_far) == len(word):
13                board[x][y] = temp
14                return True
15
16            for dx, dy in directions:
17                if 0 <= x + dx < r and 0 <= y + dy < c:
18                    if board[x + dx][y + dy] == word[len(so_far)]:
19                        ans = search(x+dx, y+dy)
20                        if ans:
21                            board[x][y] = temp
22                            return True
23            
24            board[x][y] = temp
25            so_far.pop()
26            
27            return False
28        
29        for i in range(r):
30            for j in range(c):
31                if board[i][j] == word[0] and search(i, j):
32                    return True
33        
34        return False