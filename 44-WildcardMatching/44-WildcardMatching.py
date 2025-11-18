# Last updated: 11/18/2025, 1:12:01 AM
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_idx = 0
        p_idx = 0
        s_len = len(s)
        p_len = len(p)
        
        star_idx = -1  # Last star position in pattern
        s_tmp_idx = -1  # Position in s when we last saw a star
        
        while s_idx < s_len:
            # Case 1: Characters match or pattern has '?'
            if p_idx < p_len and (p[p_idx] == '?' or s[s_idx] == p[p_idx]):
                s_idx += 1
                p_idx += 1
            
            # Case 2: Pattern has '*'
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx  # Remember star position
                s_tmp_idx = s_idx  # Remember string position
                p_idx += 1  # Move past star (assume it matches 0 chars)
            
            # Case 3: Mismatch - backtrack to last star
            elif star_idx != -1:
                p_idx = star_idx + 1  # Go back to position after star
                s_tmp_idx += 1  # Star now matches one more character
                s_idx = s_tmp_idx
            
            # Case 4: No match and no star to backtrack to
            else:
                return False
        
        # Check remaining pattern - should only contain '*'
        while p_idx < p_len and p[p_idx] == '*':
            p_idx += 1
        
        return p_idx == p_len

# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         n = len(s)
#         m = len(p)
#         dp = {}

#         def sub_match(s_index, p_index):
#             if s_index == n and p_index == m:
#                 return True
            
#             if (p_index == m and s_index < n):
#                 return False
            
#             if (s_index, p_index) in dp:
#                 return dp[(s_index, p_index)]
            
#             if s_index == n:
#                 for i in range(p_index, m):
#                     if p[i] != "*":
#                         dp[(s_index, p_index)] = False
#                         return False
                
#                 dp[(s_index, p_index)] = True
#                 return True
            
#             if p[p_index] == '?':
#                 dp[(s_index, p_index)] = sub_match(s_index + 1, p_index + 1)

#             elif p[p_index] == "*":
#                 for i in range(s_index, n + 1):
#                     if sub_match(i, p_index + 1):
#                         dp[(s_index, p_index)] = True
#                         return dp[(s_index, p_index)]
                
#                 dp[(s_index, p_index)] = False

#             elif s[s_index] == p[p_index]:
#                 dp[(s_index, p_index)] = sub_match(s_index + 1, p_index + 1)
            
#             else:
#                 dp[(s_index, p_index)] = False

#             return dp[(s_index, p_index)]
        
#         ans = sub_match(0, 0)
#         return ans