# Last updated: 4/12/2025, 2:35:01 PM
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n

        def helper(curr):
            if curr == n:
                return 1
            
            if curr > n:
                return 0
            
            if dp[curr] != -1:
                return dp[curr]

            dp[curr] = 0
            for step in [2, 1]:
                dp[curr] += helper(curr + step)
            
            return dp[curr]

        helper(0)

        return dp[0]    