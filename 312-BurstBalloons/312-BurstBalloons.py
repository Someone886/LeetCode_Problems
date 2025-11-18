# Last updated: 11/18/2025, 2:59:25 AM
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums) + 2
        vals = [1] + nums + [1]
        dp = [[0] * n for _ in range(n)]

        for dist in range(2, n):
            for starting_index in range(n - dist):
                ending_index = starting_index + dist

                for last_popped_index in range(starting_index + 1, ending_index):
                    dp[starting_index][ending_index] = \
                        max(dp[starting_index][ending_index], 
                            dp[starting_index][last_popped_index] + \
                                vals[starting_index] * vals[last_popped_index] * vals[ending_index] + \
                                dp[last_popped_index][ending_index])
        
        return dp[0][n-1]