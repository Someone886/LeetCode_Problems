# Last updated: 12/28/2025, 12:57:50 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        visited = set()
4        num = 0
5        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
6
7        for r in range(len(grid)):
8            for c in range(len(grid[0])):
9                if grid[r][c] == "1" and (r, c) not in visited:
10                    dq = deque()
11                    dq.append((r, c))
12                    visited.add((r, c))
13
14                    while dq:
15                        for _ in range(len(dq)):
16                            next_r, next_c = dq.popleft()
17
18                            for dx, dy in directions:
19                                neighbor_r, neighbor_c = next_r + dx, next_c + dy
20
21                                if 0 <= neighbor_r < len(grid) and \
22                                    0 <= neighbor_c < len(grid[0]) and \
23                                    (neighbor_r, neighbor_c) not in visited and \
24                                    grid[neighbor_r][neighbor_c] == "1":
25                                        dq.append((neighbor_r, neighbor_c))
26                                        visited.add((neighbor_r, neighbor_c))
27                    
28                    num += 1
29        
30        return num
31