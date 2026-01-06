# Last updated: 1/6/2026, 10:04:02 AM
1class Solution:
2    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
3        graph = {}
4        for i in range(len(edges)):
5            u, v = edges[i]
6            p = succProb[i]
7
8            if u not in graph:
9                graph[u] = []
10            graph[u].append((v, p))
11
12            if v not in graph:
13                graph[v] = []
14            graph[v].append((u, p))
15
16        min_q = [(1, start_node)]
17        visited = set()
18
19        while min_q:
20            p, node = heapq.heappop(min_q)
21
22            if node == end_node:
23                return -p
24
25            if node in visited:
26                continue
27            
28            visited.add(node)
29
30            if node in graph:
31                for neighbor, multiply_p in graph[node]:
32                    if neighbor not in visited:
33                        heapq.heappush(min_q, (-abs(p * multiply_p), neighbor))
34        
35        return 0