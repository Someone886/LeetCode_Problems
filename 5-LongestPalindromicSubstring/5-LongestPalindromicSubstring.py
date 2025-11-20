# Last updated: 11/20/2025, 6:02:19 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = 1
        max_left, max_right = 0, 1

        for center in range(0, n-1):
            left = center - 1
            right = center + 1

            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            length = right - left - 1
            if length > longest:
                longest = length
                max_left = left + 1
                max_right = right

            if s[center] == s[center + 1]:
                left = center
                right = center + 1

                while left >= 0 and right < n and s[left] == s[right]:
                    left -= 1
                    right += 1
                
                length = right - left - 1
                if length > longest:
                    longest = length
                    max_left = left + 1
                    max_right = right
        
        return s[max_left : max_right]
