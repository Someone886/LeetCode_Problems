# Last updated: 11/11/2025, 6:23:40 AM
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # For each iteration: 
        # 1. Identify leaves with degree = 1
        # 2. Rules out leaves from being the root of the tree
        # 3. Repeat on the rest of the tree

        # Will leave 1 or 2 possible roots remaining after the iternation -> return these possible root(s)
        if n <= 2:
            return [i for i in range(n)]
            
        adj = defaultdict(list)
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        edge_cnt = {}
        leaves = deque()
        for node, neighbors in adj.items():
            if len(neighbors) == 1:
                leaves.append(node)
            edge_cnt[node] = len(neighbors)
        
        # BFS to peel leaves layer by layer
        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                leaf = leaves.popleft()
                n -= 1
                for neighbor in adj[leaf]:
                    edge_cnt[neighbor] -= 1
                    if edge_cnt[neighbor] == 1:
                        leaves.append(neighbor)