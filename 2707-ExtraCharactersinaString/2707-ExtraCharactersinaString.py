# Last updated: 11/16/2025, 6:41:17 AM
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = {}
        n = len(s)

        def dfs(sub_s, breaking_index):
            if not sub_s:
                return 0
            
            if breaking_index in dp:
                return dp[breaking_index]

            min_left = len(sub_s)
            for word in dictionary:
                word_location = sub_s.find(word)
                if word_location != -1:
                    leftover = word_location + \
                        dfs(sub_s[word_location + len(word):], breaking_index + word_location + len(word))
                    min_left = min(min_left, leftover)
                
            dp[breaking_index] = min_left

            return min_left

        ans = dfs(s, 0)
        return ans