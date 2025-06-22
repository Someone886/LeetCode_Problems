# Last updated: 6/22/2025, 2:50:47 PM
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        n = len(piles)
        piles_sum = sum(piles)

        def helper(index, M):
            if index >= n:
                return 0
            
            if (index, M) in dp:
                return dp[(index, M)]
            
            max_diff = float("-inf")
            running_sum = 0
            for x in range(0, 2 * M):
                if index + x >= n:
                    break
                running_sum += piles[index + x]
                max_diff = max(max_diff, running_sum - helper(index + x + 1, max(M, x + 1)))
            
            dp[(index, M)] = max_diff
            return max_diff
        
        alice_max_diff = helper(0, 1)
        return (piles_sum + alice_max_diff) // 2