# Last updated: 1/6/2026, 11:19:07 AM
1class Solution:
2    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
3        m, n = len(mat), len(mat[0])
4        dq = deque()
5        visited = [[False] * n for _ in range(m)]
6        
7        # 1. Add all '0's to the queue and mark them as visited
8        for i in range(m):
9            for j in range(n):
10                if mat[i][j] == 0:
11                    dq.append((i, j))
12                    visited[i][j] = True
13        
14        dist = 0
15        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
16        
17        # 2. Process BFS in waves
18        while dq:
19            # Everything currently in the queue is at distance 'dist'
20            for _ in range(len(dq)):
21                r, c = dq.popleft()
22                
23                # Update the matrix with the current distance
24                mat[r][c] = dist
25                
26                for dr, dc in directions:
27                    nr, nc = r + dr, c + dc
28                    
29                    # Boundary check and visited check
30                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
31                        visited[nr][nc] = True
32                        dq.append((nr, nc))
33            
34            # Increment distance for the next wave
35            dist += 1
36            
37        return mat