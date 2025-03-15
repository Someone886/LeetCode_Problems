class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        
        def fact(n):
            mul = 1
            for i in range(1, n+1):
                mul *= i
            return mul
    
        return int(fact(m-1 + n-1) / (fact(n - 1) * fact(m - 1)))