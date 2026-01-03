# Last updated: 1/3/2026, 11:41:25 AM
1class Solution:
2    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
3        # 1. BUILD THE GRAPH
4        # We use an adjacency list where adj[node] = [(neighbor, weight), ...]
5        adj = defaultdict(list)
6
7        for i, equation in enumerate(equations):
8            u, v = equation
9            val = values[i]
10            # Forward edge: u / v = val
11            adj[u].append([v, val])
12            # Backward edge: v / u = 1 / val
13            adj[v].append([u, 1 / val])
14
15        # 2. DEFINE THE SEARCH (DFS)
16        def dfs(start, end, visited):
17            # Base Case 1: If we reach the target node, the multiplier is 1
18            if start == end:
19                return 1
20            
21            # Mark the current node as visited to avoid infinite loops (cycles)
22            visited.add(start)
23
24            # Explore neighbors
25            for neighbor, value in adj[start]:
26                if neighbor in visited:
27                    continue
28                
29                # Recursively search for a path to the 'end' node
30                dfs_result = dfs(neighbor, end, visited)
31                
32                # If a valid path (non-zero result) is found, 
33                # multiply the current edge weight by the result from the rest of the path
34                if dfs_result != 0:
35                    return value * dfs_result
36            
37            # Base Case 2: No path found from this node
38            return 0
39
40        # 3. PROCESS QUERIES
41        all_ans = []
42
43        for query in queries:
44            numerator, denominator = query
45
46            # Edge Case: If the variable hasn't been seen before, the result is -1.0
47            if numerator not in adj or denominator not in adj:
48                all_ans.append(-1.0)
49                
50            else:
51                # Initialize a new visited set for every query
52                visited = set()
53                query_ans = dfs(numerator, denominator, visited)
54
55                # If DFS returned 0, it means no path exists between the variables
56                if query_ans != 0:
57                    all_ans.append(query_ans)
58                else:
59                    all_ans.append(-1.0)
60
61        return all_ans