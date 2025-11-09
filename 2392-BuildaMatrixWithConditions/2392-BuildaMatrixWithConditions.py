# Last updated: 11/9/2025, 3:03:27 AM
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Topo sort + DFS.
        # Either the row graph or the col graph has a cycle, then the setting is INVALID.

        # Topo sort also works on disconnected graph

        # DFS: (1) Add the leaf node to the beginning of the output, then the node without unvisited children.
        #      (2) Then reverse the output.
        #      (3) Visited records visited nodes. 
        #          Visiting a visited node != a cycle necessarily.
        #          Path records nodes on the path and will be removed after visiting. 
        #          Visiting a path node = cycle.
        #          Order records the order to visit each of the k nodes
        # BFS cannot be used to contruct a PATH.

        def dfs(src, adj, visited, path, order):
            # If the path returns to the src, then this is an cycle.
            if src in path:
                return False
            # If the path returns to a visited node, then just skip it and its children.
            if src in visited:
                return True
            
            visited.add(src)
            path.add(src)

            for nei in adj[src]:
                if not dfs(nei, adj, visited, path, order):
                    return False
            
            order.append(src)
            path.remove(src)
            return True

        def topo_sort(edges):
            # convert edges to the adj hashmap
            adj = defaultdict(list)
            for src, dst in edges:
                adj[src].append(dst)
            
            # Visited records visited nodes. Visiting a visited node != a cycle necessarily.
            # path records nodes on the path and will be removed after visiting. Visiting a path node = cycle.
            # order records the order to visit each of the k nodes

            visited, path = set(), set()
            order = []
            for src in range(1, k + 1):
                if not dfs(src, adj, visited, path, order):
                    return []
            
            return order[::-1]
        
        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        if not row_order or not col_order:
            return []

        board = [[0] * k for _ in range(k)]        
        row_filling = {num: i for i, num in enumerate(row_order)}
        col_filling = {num: i for i, num in enumerate(col_order)}

        for num in range(1, k + 1):
            board[row_filling[num]][col_filling[num]] = num
        
        return board
