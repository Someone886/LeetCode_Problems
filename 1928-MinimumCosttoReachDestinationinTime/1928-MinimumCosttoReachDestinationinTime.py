# Last updated: 1/3/2026, 5:35:49 PM
1class Solution:
2    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
3        n = len(passingFees)
4        graph = {}
5        for u, v, t in edges:
6            if u not in graph: graph[u] = []
7            graph[u].append((v, t))
8            if v not in graph: graph[v] = []
9            graph[v].append((u, t))
10        
11        # min_times[node] stores the minimum time reached for this node so far.
12        # We only revisit a node if we can reach it faster than before.
13        min_times = [(maxTime + 1) for _ in range(n)]
14        
15        # Priority Queue: (total_fee, current_time, node)
16        # Dijkstra's will naturally pick the cheapest fee first.
17        min_q = [(passingFees[0], 0, 0)]
18        min_times[0] = 0
19
20        while min_q:
21            fee, time, node = heapq.heappop(min_q)
22            
23            # If we reached the destination, because it's a min-heap on fee,
24            # this is guaranteed to be the minimum fee for this time.
25            if node == n - 1:
26                return fee
27            
28            # One cannot skip if time > min_times[node] here
29            # Check this example: https://gemini.google.com/share/f01e5969457f
30            # Reasoning: min_times[node] can be edited after a path is pushed to the min_q
31            # with lower fees but higher time than the edited min_times[node]
32            
33            if node in graph:
34                for neighbor, t in graph[node]:
35                    new_time = time + t
36                    
37                    # Only proceed if we found a faster way to get to the neighbor.
38                    if new_time < min_times[neighbor]:
39                        min_times[neighbor] = new_time
40                        heapq.heappush(min_q, (fee + passingFees[neighbor], new_time, neighbor))
41        
42        return -1