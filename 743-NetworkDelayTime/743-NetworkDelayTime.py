# Last updated: 4/21/2025, 1:29:36 AM
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u, v, t in times:
            edges[u].append((v, t))
        
        # min_heap keeps len(path) to the node i from the start node k
        min_heap = [(0, k)]
        visit = set()
        t = 0   # result to be returned -> total length

        while min_heap:
            w_1, n_1 = heapq.heappop(min_heap)
            if n_1 in visit:
                continue
            else:
                visit.add(n_1)
            
            t = w_1

            for neighbor, weight in edges[n_1]:
                heapq.heappush(min_heap, (w_1 + weight, neighbor))
        
        return t if len(visit) == n else -1