# Last updated: 4/4/2025, 12:45:16 AM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)
        res = upper

        while upper >= lower:
            curr_rate = (lower + upper) // 2
            time_needed = sum([math.ceil(pile / curr_rate) for pile in piles])

            if time_needed <= h:
                res = curr_rate
                upper = curr_rate - 1

            else:
                lower = curr_rate + 1
                
        return res
        