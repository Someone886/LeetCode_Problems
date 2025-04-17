class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        dp = {}

        # index i and j are the chars to be munipulated
        def helper(i, j):
            k = i + j

            if k == len(s3):
                return True
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            ans = False
            if i < len(s1) and s1[i] == s3[k]:
                ans = helper(i + 1, j)
            
            if not ans:
                if j < len(s2) and s2[j] == s3[k]:
                    ans = helper(i, j + 1)
            
            dp[(i, j)] = ans
            return ans
        
        return helper(0, 0)
