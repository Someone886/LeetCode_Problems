# Last updated: 1/4/2026, 5:23:06 PM
1class Solution:
2    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
3        if not grid or grid[0][0] or grid[-1][-1] != 0:
4            return -1
5        
6        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, -1), (-1, 1)]
7
8        n = len(grid)
9        dq = deque()
10        dq.append((0, 0))
11        visited = set()
12        visited.add((0, 0))
13        steps = 1
14
15        while dq:
16            for _ in range(len(dq)):
17                r, c = dq.popleft()
18
19                if r == n - 1 and c == n - 1:
20                    return steps
21                
22                for dr, dc in directions:
23                    new_r, new_c = r + dr, c + dc
24
25                    if (new_r, new_c) in visited:
26                        continue
27                    
28                    if 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c] == 0:
29                        visited.add((new_r, new_c))
30                        dq.append((new_r, new_c))
31            
32            steps += 1
33        
34        return -1