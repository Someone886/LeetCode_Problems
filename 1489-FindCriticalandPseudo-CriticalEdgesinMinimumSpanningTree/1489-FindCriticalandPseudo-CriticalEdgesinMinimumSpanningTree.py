# Last updated: 11/8/2025, 1:15:00 AM
class Union_Find:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        
        return node
    
    # return True if not same, False if same parent
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)

        if parent1 == parent2:
            return False
        
        if self.size[parent1] > self.size[parent2]:
            self.parent[parent2] = parent1
            self.size[parent1] += self.size[parent2]
        else:
            self.parent[parent1] = parent2
            self.size[parent2] += self.size[parent1]
        
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 1. Run Kruskal's algo once to find the MST
        # 2. Remove each edge, and get another MST
        # 3. If total weights of the MST increase, then this edge is critical

        # 4. An edge is critical, then this edge cannot be pseudo-critical
        # 5. To check an edge is pseudo-critical, after we ensure this edge is not critical
        # we can test if including this edge will still output MST.
        # 6. If so, then this edge is pseudo-critical.

        for i, edge in enumerate(edges):
            edge.append(i) # edge = (u, v, weight, original_index of the edge)
        
        edges.sort(key = lambda edge: edge[2])
        mst_weight = 0

        uf = Union_Find(n)
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mst_weight += w
        
        critical, pseudo_critical = [], []

        for node1, node2, edge_weight, i in edges:
            # Try finding the MST without the edge i
            new_mst_weight = 0

            uf = Union_Find(n)
            for other_node1, other_node12, w1, j in edges:
                if j == i: # skip edge i
                    continue

                if uf.union(other_node1, other_node12):
                    new_mst_weight += w1
        
            if new_mst_weight < mst_weight or new_mst_weight > mst_weight: 
            # if max(uf.size) != n or new_mst_weight > mst_weight:
                critical.append(i)
                continue
            
            # if this edge is not critical, check if it is pseudo-critical
            uf = Union_Find(n)
            new_mst_weight = edge_weight
            uf.union(node1, node2)

            for other_node1, other_node12, w1, j in edges:
                if j == i: # skip edge i as it is already included above
                    continue

                if uf.union(other_node1, other_node12):
                    new_mst_weight += w1

            if new_mst_weight == mst_weight:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]