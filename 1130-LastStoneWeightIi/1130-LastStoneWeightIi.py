# Last updated: 6/22/2025, 2:50:50 PM
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target  = (stone_sum + 1) // 2
        dp = {}

        # keep track of the index and the sum of current pile of stones
        def dfs(index, current_sum):
            if current_sum >= target or index == len(stones):
                return abs(current_sum - (stone_sum - current_sum))
            
            if (index, current_sum) in dp:
                return dp[(index, current_sum)]
            
            # a stone is either classified to be this pile (current_sum) or that pile (total - current_sum)
            dp[(index, current_sum)] = min(dfs(index + 1, current_sum + stones[index]), dfs(index + 1, current_sum))
            return dp[(index, current_sum)]

        ans = dfs(0, 0)
        return ans