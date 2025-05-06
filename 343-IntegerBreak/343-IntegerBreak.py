# Last updated: 5/5/2025, 10:25:49 PM

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1

        for num in range(2, n + 1):
            dp[num] = 0 if num == n else num # must split at the top level where num = n
            for i in range(1, num):
                dp[num] = max(dp[num], dp[i] * dp[num - i])
        return dp[n]


'''
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [-1] * (n + 1)

        def helper(left):
            if left == 0:
                return 1
            
            if dp[left] != -1:
                return dp[left]
            
            max_product = left
            for i in range(1, left // 2 + 1):
                max_product = max(max_product, i * helper(left - i))
            dp[left] = max_product

            return dp[left]
        
        # but for the *original* n we *must* split at least once:
        best = 0
        for i in range(1, n//2 + 1):
            best = max(best, i * helper(n - i))
        return best
'''