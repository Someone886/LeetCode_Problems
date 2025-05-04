# Last updated: 5/4/2025, 12:15:48 AM
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = min_capacity = max(weights)
        r = max_capacity = sum(weights)

        def can_ship(capacity):
            ships = 1
            curr_ship_weight = 0

            for w in weights:
                if curr_ship_weight + w > capacity:
                    ships += 1
                    curr_ship_weight = 0
                curr_ship_weight += w
            
            return ships <= days

        while l <= r:
            m = (l + r) // 2
            if can_ship(m):
                r = m - 1
            else:
                l = m + 1
            
        return l