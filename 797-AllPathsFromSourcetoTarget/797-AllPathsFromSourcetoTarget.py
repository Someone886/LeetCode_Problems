# Last updated: 1/3/2026, 7:09:21 PM
1class Solution:
2    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
3        res = []
4        dq = deque()
5        dq.append((0, []))
6        n = len(graph)
7
8        while dq:
9            node, path = dq.popleft()
10            
11            path = path + [node]
12            if node == n - 1:
13                res.append(path)
14                continue
15            
16            for neighbor in graph[node]:
17                dq.append((neighbor, path))
18
19        return res