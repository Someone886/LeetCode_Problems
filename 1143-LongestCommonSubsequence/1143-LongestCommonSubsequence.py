# Last updated: 4/16/2025, 1:53:31 PM
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len_1 = len(text1)
        len_2 = len(text2)

        dp = [[-1] * len_1 for _ in range(len_2)]

        def helper(index_1, index_2):
            if index_1 == len_1 or index_2 == len_2:
                return 0
            
            if dp[index_2][index_1] != -1:
                return dp[index_2][index_1]
            
            if_same = 1 if text1[index_1] == text2[index_2] else 0

            if if_same:
                dp[index_2][index_1] = 1 + helper(index_1 + 1, index_2 + 1)
            else:
                dp[index_2][index_1] = max(helper(index_1 + 1, index_2), helper(index_1, index_2 + 1))
            
            return dp[index_2][index_1]

        return helper(0, 0)
