# Last updated: 11/18/2025, 1:19:22 AM
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def helper(index_s, index_p):
            if index_s == len(s) and index_p == len(p):
                return True
            
            if index_p >= len(p):
                return False
            
            if (index_s, index_p) in dp:
                return dp[(index_s, index_p)]
            
            if index_s == len(s):
                if index_p < len(p) - 1 and p[index_p + 1] == "*":
                    dp[(index_s, index_p)] = helper(index_s, index_p + 2)
                    return dp[(index_s, index_p)]
                else:
                    return False
            
            if index_p < len(p) - 1 and p[index_p + 1] == "*":
                if (p[index_p] == '.' or s[index_s] == p[index_p]):
                    dp[(index_s, index_p)] = helper(index_s + 1, index_p) or \
                                                helper(index_s, index_p + 2)
                else:
                    dp[(index_s, index_p)] = helper(index_s, index_p + 2)
            
            else:
                if (p[index_p] == '.' or s[index_s] == p[index_p]):
                    dp[(index_s, index_p)] = helper(index_s + 1, index_p + 1)
                else:
                    dp[(index_s, index_p)] = False
            
            return dp[(index_s, index_p)]
        
        ans = helper(0, 0)
        return ans