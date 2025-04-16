# Last updated: 4/15/2025, 9:15:03 PM
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        index = 0
        for n1, n2 in edges:
            adj[n1].append([n2, index])
            adj[n2].append([n1, index])
            index += 1
        
        visited = set()
        path = []

        def dfs(node, prev, order):
            path.append([prev, node, order])

            if node in visited:
                return True

            visited.add(node)

            for neighbor, i in adj[node]:
                if neighbor != prev:
                    if dfs(neighbor, node, i):
                        return True
            
            path.pop()
            return False
        
        dfs(1, 0, -1)
        
        cycle_end, cycle_start, _ = path[-1]
        in_cycle = False

        ans = path[0][0:2]
        max_order = path[0][2]
        
        # print(path)

        for i in range(1, len(path)):
            node, prev, order = path[i]

            if node == cycle_start:
                in_cycle = True

            if not in_cycle:
                continue

            if order > max_order:
                ans = [node, prev]
                max_order = order

        return [ans[0], ans[1]] if ans[0] < ans[1] else [ans[1], ans[0]]