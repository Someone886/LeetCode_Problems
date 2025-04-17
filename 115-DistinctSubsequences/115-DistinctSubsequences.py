# Last updated: 4/17/2025, 1:19:32 AM
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def helper(index_1, index_2):
            if index_2 == len(t):
                return 1
            
            if index_1 == len(s):
                return 0
            
            if len(s) - index_1 < len(t) - index_2:
                return 0
            
            if (index_1, index_2) in dp:
                return dp[index_1, index_2]
            
            if s[index_1] == t[index_2]:
                dp[(index_1, index_2)] = helper(index_1 + 1, index_2) + helper(index_1 + 1, index_2 + 1)

            else:
                dp[(index_1, index_2)] = helper(index_1 + 1, index_2)
            
            return dp[(index_1, index_2)]
        
        ans = helper(0, 0)
        return ans
