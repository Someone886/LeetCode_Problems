# Last updated: 5/14/2025, 8:25:13 PM
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else: # if not, check if it is after removing either right of left value
                return s[left:right] == s[left:right][::-1] or s[left+1:right+1] == s[left+1:right+1][::-1]
        
        return True


# class Solution:
#     def validPalindrome(self, s: str) -> bool:
        
#         def helper(l, r, deleted):
#             if l >= r:
#                 return True
            
#             if s[l] == s[r]:
#                 return helper(l + 1, r - 1, deleted)
#             else:
#                 if deleted:
#                     return False
#                 else:
#                     return helper(l + 1, r, True) or helper(l, r - 1, True)
        
#         return helper(0, len(s) - 1, False)