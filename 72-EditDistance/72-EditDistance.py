# Last updated: 4/17/2025, 1:56:21 AM
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def helper(index_1, index_2):
            if index_2 == len(word2):
                return len(word1) - index_1
            
            if index_1 == len(word1):
                return len(word2) - index_2
            
            if (index_1, index_2) in dp:
                return dp[(index_1, index_2)]
            
            if word1[index_1] == word2[index_2]:
                dp[(index_1, index_2)] = helper(index_1 + 1, index_2 + 1)
            
            else:
                dp[(index_1, index_2)] = 1 + min(helper(index_1 + 1, index_2 + 1),
                                                 helper(index_1, index_2 + 1), 
                                                 helper(index_1 + 1, index_2))

            return dp[(index_1, index_2)]
        
        ans = helper(0, 0)
        return ans