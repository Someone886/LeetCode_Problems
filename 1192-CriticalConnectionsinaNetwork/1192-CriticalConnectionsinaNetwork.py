# Last updated: 1/12/2026, 2:17:50 PM
1class Solution:
2    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
3        # Graph building (kept exactly as your original version)
4        graph = {}
5        for u, v in connections:
6            if u not in graph:
7                graph[u] = []
8            graph[u].append(v)
9            if v not in graph:
10                graph[v] = []
11            graph[v].append(u)
12
13        # jump[i] stores the discovery 'depth' of node i.
14        # It's like a timestamp: "I was visited at depth X."
15        jump = [-1] * n
16        res = []
17
18        def dfs(curr, parent, depth):
19            # 1. MARK DISCOVERY: Record the depth we reached this node at.
20            jump[curr] = depth
21            
22            # 2. TRACKING THE "BACKDOOR": 
23            # 'lowest_reachable' tracks the highest ancestor (minimum depth)
24            # that this node or any of its descendants can reach.
25            # Initially, the best a node can reach is itself.
26            lowest_reachable = depth
27
28            for child in graph.get(curr, []):
29                if child == parent:
30                    continue
31                
32                if jump[child] == -1:
33                    # RECURSIVE SEARCH: Explore the subtree below this 'child'.
34                    # It returns the best "backdoor" depth that subtree found.
35                    subtree_best_jump = dfs(child, curr, depth + 1)
36                    
37                    # BRIDGE CONDITION: 
38                    # If the BEST depth the subtree could reach is still DEEPER 
39                    # than my current depth, it means there is NO back-edge 
40                    # from that subtree to me or my ancestors. 
41                    # The edge (curr, child) is the ONLY path!
42                    if subtree_best_jump > depth:
43                        res.append([curr, child])
44                    
45                    # Update current node's best reach based on what child found.
46                    lowest_reachable = min(lowest_reachable, subtree_best_jump)
47                else:
48                    # CYCLE DETECTED: We found a 'back-edge' to an already visited node.
49                    # This node might be an ancestor, providing a shortcut.
50                    lowest_reachable = min(lowest_reachable, jump[child])
51
52            # Return the best shortcut found in this entire branch to the parent.
53            return lowest_reachable
54        
55        # Start DFS from the first node at depth 0.
56        dfs(0, -1, 0)
57        return res