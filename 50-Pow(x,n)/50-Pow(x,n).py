class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n == 1:
            return x
        
        if n == -1:
            return 1/x

        if x == 1:
            return x
        
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        
        negative = False
        if n < 0:
            x = 1/x
            negative = True
            n = -n-1
        
        ans = 1
        temp = x

        while (n != 0):
            if n % 2 == 1:
                ans *= temp
            temp *= temp
            n = n // 2

        if negative:
            ans = ans * x

        return ans