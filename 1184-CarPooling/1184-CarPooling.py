# Last updated: 6/22/2025, 2:50:49 PM
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])
        curr_num = 0
        curr_capacity = 0
        capacity_queue = []
        heapq.heapify(capacity_queue)

        for trip in trips:
            num_i, from_i, to_i = trip

            if not capacity_queue:
                if num_i > capacity:
                    return False
                curr_capacity += num_i
                heapq.heappush(capacity_queue, [to_i, num_i])

            else:
                curr_capacity += num_i
                if curr_capacity <= capacity:
                    heapq.heappush(capacity_queue, [to_i, num_i])

                else:
                    while curr_capacity > capacity:
                        next_to, next_num = heapq.heappop(capacity_queue)
                        
                        if next_to > from_i:
                            return False
                        
                        curr_capacity -= next_num
                    heapq.heappush(capacity_queue, [to_i, num_i])
                        
        return True
                    
            