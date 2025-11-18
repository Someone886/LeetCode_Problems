# Last updated: 11/18/2025, 3:59:14 AM
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
            
        len1 = len(s1)
        len2 = len(s2)
        dp = {}

        def sub_interleave(index1, index2):
            if index1 == len1:
                return s2[index2:] == s3[len1 + index2:]
            
            if index2 == len2:
                return s1[index1:] == s3[len2 + index1:]
            
            if (index1, index2) in dp:
                return dp[(index1, index2)]
            
            dp[(index1, index2)] = False
            if s1[index1] == s3[index1 + index2]:
                dp[(index1, index2)] = sub_interleave(index1 + 1, index2)
            
            if not dp[(index1, index2)] and s2[index2] == s3[index1 + index2]:
                dp[(index1, index2)] = sub_interleave(index1, index2 + 1)
            
            return dp[(index1, index2)]
        
        ans = sub_interleave(0, 0)
        return ans
            
