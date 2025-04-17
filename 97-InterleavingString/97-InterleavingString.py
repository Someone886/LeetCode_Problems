# Last updated: 4/16/2025, 9:04:11 PM
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        dp = {}
        len_1 = len(s1)
        len_2 = len(s2)

        # index_1 and index_2 are the chars to be munipulated

        def helper(index_1, index_2, string_index):
            if index_1 == len_1:
                ans = s2[index_2:] == s3[index_1 + index_2:]
                dp[(index_1, index_2, string_index)] = ans
                return ans
                
            if index_2 == len_2:
                ans = s1[index_1:] == s3[index_1 + index_2:]
                dp[(index_1, index_2, string_index)] = ans
                return ans
            
            if (index_1, index_2, string_index) in dp:
                return dp[(index_1, index_2, string_index)]
            
            index_3 = index_1 + index_2
            if string_index == 1:
                if s3[index_3] != s1[index_1]:
                    return False
                else:
                    dp[(index_1, index_2, string_index)] = helper(index_1 + 1, index_2, 1) or\
                                                           helper(index_1 + 1, index_2, 2)
            
            elif string_index == 2:
                if s3[index_3] != s2[index_2]:
                    return False
                else:
                    dp[(index_1, index_2, string_index)] = helper(index_1, index_2 + 1, 2) or\
                                                           helper(index_1, index_2 + 1, 1)
            
            return dp[(index_1, index_2, string_index)]
        
        ans = helper(0, 0, 1) or helper(0, 0, 2)
        return ans