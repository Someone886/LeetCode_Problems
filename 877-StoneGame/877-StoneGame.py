# Last updated: 5/7/2025, 12:33:02 AM
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        n = len(piles)

        def helper(front_index, back_index):
            if front_index == back_index:
                return piles[front_index]
            
            if (front_index, back_index) in dp:
                return dp[(front_index, back_index)]
            
            max_diff = max(piles[front_index] - helper(front_index + 1, back_index),\
                           piles[back_index] - helper(front_index, back_index - 1))
            
            dp[(front_index, back_index)] = max_diff
            return max_diff
        
        ans = helper(0, n - 1)
        return True if ans > 0 else False

# actually Alice always wins -> return True lol