# Last updated: 4/19/2025, 4:59:18 PM
class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        first = True

        while first or slow != fast:
            first = False
            
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
        return True if fast == 1 else False
    
    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output