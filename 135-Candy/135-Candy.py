# Last updated: 11/13/2025, 6:27:05 PM
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # first pass from left to right: 
        #   child at index i has more candies than its left neighbor if child i has a higher ranking
        # second pass from right to left:
        #   child at index i has more candies than its right neighbor if child i has a higher ranking

        n = len(ratings)
        candies = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = max(candies[i], candies[i - 1] + 1)
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


# heapq with nlogn:

# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         n = len(ratings)
#         candies = [1] * n

#         q = [(ranking, index) for index, ranking in enumerate(ratings)]
#         heapq.heapify(q)

#         while q:
#             child_ranking, child_index = heapq.heappop(q)
            
#             if child_index - 1 >= 0:
#                 if child_ranking < ratings[child_index - 1]:
#                     candies[child_index - 1] = max(candies[child_index - 1], 1 + candies[child_index])

#             if child_index + 1 <= n - 1:
#                 if child_ranking < ratings[child_index + 1]:
#                     candies[child_index + 1] = max(candies[child_index + 1], 1 + candies[child_index])
        
#         return sum(candies)