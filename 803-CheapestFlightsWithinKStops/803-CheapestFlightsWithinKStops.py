# Last updated: 6/22/2025, 2:51:03 PM
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = defaultdict(list)
        for start, end, price in flights:
            edges[start].append((end, price))
        
        q = deque()
        # dp in q: node, cost to reach this node from src, stop count
        q.append([src, 0, -1])
        cost = float('inf')

        costs = [float('inf')] * n
        costs[src] = 0

        while q:
            start, cost_so_far, stop = q.popleft()
            if stop >= k:
                continue

            for neighbor, price in edges[start]:
                new_cost = cost_so_far + price
                if new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    q.append([neighbor, new_cost, stop + 1])
        
        return -1 if costs[dst] == float("inf") else costs[dst]