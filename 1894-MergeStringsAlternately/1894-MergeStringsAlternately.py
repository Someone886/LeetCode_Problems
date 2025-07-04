# Last updated: 6/22/2025, 2:50:40 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        p1, p2 = 0, 0

        while p1 < len(word1) and p2 < len(word2):
            ans += word1[p1]
            ans += word2[p2]

            p1 += 1
            p2 += 1
        
        ans += word1[p1:]
        ans += word2[p2:]

        return ans