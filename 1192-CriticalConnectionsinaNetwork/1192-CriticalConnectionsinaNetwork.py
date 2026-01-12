# Last updated: 1/12/2026, 3:08:06 PM
1import math
2from collections import deque
3
4class Solution:
5    def maximumDetonation(self, bombs: list[list[int]]) -> int:
6        n = len(bombs)
7        adj = [[] for _ in range(n)]
8
9        # 1. Build the Directed Graph
10        for i in range(n):
11            x1, y1, r1 = bombs[i]
12            for j in range(n):
13                if i == j: 
14                    continue
15                
16                x2, y2, r2 = bombs[j]
17                
18                # Euclidean distance squared (to avoid slow sqrt)
19                dist_sq = (x1 - x2)**2 + (y1 - y2)**2
20                
21                # If distance <= radius of bomb i, i can detonate j
22                if dist_sq <= r1**2:
23                    adj[i].append(j)
24
25        # 2. BFS Function
26        def bfs(start_node):
27            q = deque([start_node])
28            visited = {start_node}
29            
30            while q:
31                curr = q.popleft()
32                for neighbor in adj[curr]:
33                    if neighbor not in visited:
34                        visited.add(neighbor)
35                        q.append(neighbor)
36            return len(visited)
37
38        # 3. Try detonating every bomb and find the max
39        max_bombs = 0
40        for i in range(n):
41            max_bombs = max(max_bombs, bfs(i))
42            
43        return max_bombs