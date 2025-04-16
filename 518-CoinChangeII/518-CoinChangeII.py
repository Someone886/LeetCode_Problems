# Last updated: 4/16/2025, 7:35:18 PM
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][-1] = 1
        
        for i in range(n - 1, -1, -1):
            for total in range(amount, -1, -1):
                if total <= amount - coins[i]:
                    dp[i][total] = dp[i + 1][total] + dp[i][total + coins[i]]
        
        return dp[0][0]