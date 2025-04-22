# Last updated: 4/22/2025, 2:37:13 AM
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        recorded_points = []

        for point in points:
            for i in range(len(recorded_points)):
                recorded_point = recorded_points[i]
                dist = abs(point[0] - recorded_point[0]) + abs(point[1] - recorded_point[1])
                edges.append((dist, i, len(recorded_points)))
            recorded_points.append(point)
        
        edges.sort()

        n = len(recorded_points)
        parents = [i for i in range(n)]
        size = [1] * n

        def find(n):
            parent = parents[n]
            while parent != parents[parent]:
                parents[parent] = parents[parents[parent]]
                parent = parents[parent]
            
            return parent
        
        def union(u, v):
            parent_1, parent_2 = find(u), find(v)
            if parent_1 == parent_2:
                return False
            
            if size[parent_1] > size[parent_2]:
                size[parent_1] += size[parent_2]
                parents[parent_2] = parent_1
            else:
                size[parent_2] += size[parent_1]
                parents[parent_1] = parent_2
            
            return True
        
        total_length = 0

        for dist, u, v in edges:
            if not union(u, v):
                continue
            else:
                total_length += dist

        return total_length