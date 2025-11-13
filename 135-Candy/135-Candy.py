# Last updated: 11/13/2025, 5:58:58 PM
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        q = [(ranking, index) for index, ranking in enumerate(ratings)]
        heapq.heapify(q)

        while q:
            child_ranking, child_index = heapq.heappop(q)
            
            if child_index - 1 >= 0:
                if child_ranking < ratings[child_index - 1]:
                    candies[child_index - 1] = max(candies[child_index - 1], 1 + candies[child_index])

            if child_index + 1 <= n - 1:
                if child_ranking < ratings[child_index + 1]:
                    candies[child_index + 1] = max(candies[child_index + 1], 1 + candies[child_index])
        
        return sum(candies)