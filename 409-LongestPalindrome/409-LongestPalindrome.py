# Last updated: 4/12/2025, 11:01:42 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        max_interval = [0, 1]
        n = len(s)

        for center in range(0, n - 1):
            l, r = center - 1, center + 1
            while l >= 0 and r <= n - 1:
                if s[l] != s[r]:
                    break

                l -= 1
                r += 1
            
            length = (r-1) - (l+1) + 1
            if length > max_len:
                max_len = length
                max_interval = [l + 1, r]
            
            l, r = center, center + 1
            while l >= 0 and r <= n - 1:
                if s[l] != s[r]:
                    break

                l -= 1
                r += 1
            
            length = (r-1) - (l+1) + 1
            if length > max_len:
                max_len = length
                max_interval = [l + 1, r]
        
        return s[max_interval[0] : max_interval[1]]