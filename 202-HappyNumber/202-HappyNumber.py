class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        fast = self.sumOfSquares(fast)
        fast = self.sumOfSquares(fast)

        while slow != fast:
            if fast == 1:
                return True
            
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