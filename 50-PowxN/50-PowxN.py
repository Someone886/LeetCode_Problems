# Last updated: 6/22/2025, 2:53:21 PM
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        if n == 0:
            return 1
        
        ans = 1
        power = abs(n)

        while power:
            if power % 2 == 1:
                ans *= x
            x *= x
            power = power // 2
        
        return ans if n > 0 else 1 / ans