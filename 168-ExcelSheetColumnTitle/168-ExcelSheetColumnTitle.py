# Last updated: 5/18/2025, 2:32:22 AM
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result = chr(remainder + ord('A')) + result
            columnNumber //= 26
        return result

'''
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""

        while columnNumber > 26:
            remainder = columnNumber % 26
            if remainder == 0:
                remainder = 26
            ans += chr(ord("A") + remainder - 1)
            columnNumber = (columnNumber - 1) // 26
        
        remainder = columnNumber
        if remainder == 0:
            remainder = 26
        ans += chr(ord("A") + remainder - 1)
        
        return ans[::-1]
'''