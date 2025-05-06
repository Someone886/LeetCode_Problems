# Last updated: 5/5/2025, 9:50:11 PM
import math

class Solution:
    def numSquares(self, n: int) -> int:
        # O(n * sqrt(n))

        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s ** 2
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])
        
        return dp[n]

'''
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [-1] * (n + 1)

        def helper(left):
            if left == 0:
                return 0
            
            if left < 0:
                return float('inf')
            
            if dp[left] != -1:
                return dp[left]
            
            upper_bound = int(math.sqrt(left))
            min_cnt = float('inf')
            for i in range(upper_bound, 0, -1):
                min_cnt = min(min_cnt, 1 + helper(left - i**2))
            
            dp[left] = min_cnt
            return min_cnt
        
        ans = helper(n)
        return ans
'''