# Last updated: 4/13/2025, 8:49:08 AM
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [-1] * n

        def helper(curr):
            if curr == n:
                return 1
            
            if dp[curr] != -1:
                return dp[curr]
            
            len_left = n - curr
            dp[curr] = 0
            for word in wordDict:
                len_word = len(word)
                if len_word > len_left:
                    continue
                
                if s[curr:curr + len_word] == word:
                    dp[curr] = helper(curr + len_word)
                    if dp[curr] == 1:
                        return dp[curr]
            
            return dp[curr]
        
        ans = helper(0)
        return ans == 1