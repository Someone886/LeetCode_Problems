class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u, v, t in times:
            edges[u].append((v, t))
        
        # min_heap keeps len(path) to the node i from the start node k
        min_heap = [(0, k)]
        visit = set()

        # everytime adds the shortest node from the start node k to the explored graph
        # after exploring node i, add its neighbors to the heap
        # ~ BFS
        while min_heap:
            l, node = heapq.heappop(min_heap)
            
            if node in visit:
                continue
            else:
                visit.add(node)
            
            if len(visit) == n:
                return l

            for neighbor, weight in edges[node]:
                if neighbor not in visit:
                    heapq.heappush(min_heap, (l + weight, neighbor))
        
        return -1
        