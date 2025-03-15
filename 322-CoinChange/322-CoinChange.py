class Solution:
  def coinChange(self, coins, amount):
    INVALID = amount + 1
    dp = [INVALID] * (amount + 1)
    dp[0] = 0
    for coin in coins:
      for i in range(coin, amount + 1):
        if dp[i] > dp[i - coin] + 1: 
            dp[i] = dp[i - coin] + 1
    return -1 if dp[amount] == INVALID else dp[amount]
        