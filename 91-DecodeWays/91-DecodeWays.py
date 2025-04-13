# Last updated: 4/13/2025, 5:35:51 AM
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)
        n = len(s)

        def helper(start, end):
            if start >= n:
                return 0
            
            if end > n:
                return 0

            if s[start] == '0':
                return 0
            
            num = int(s[start:end])
            if num > 26:
                return 0

            if end == n:
                return 1
            
            if dp[end] != -1:
                return dp[end]
            
            dp[end] = helper(end, end + 1) + helper(end, end + 2)
            return dp[end]
        
        ans = helper(0, 1) + helper(0, 2)
        return ans