# Last updated: 6/22/2025, 2:50:59 PM
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
        