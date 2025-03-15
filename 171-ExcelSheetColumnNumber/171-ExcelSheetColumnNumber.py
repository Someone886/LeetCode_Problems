class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        start = ord('A')
        n = len(columnTitle)
        ans = 0
        
        for i in range(n - 1, -1, -1):
            char = columnTitle[i]
            ans += (ord(char) - start + 1) * (26 ** (n - 1 - i))
        
        return ans