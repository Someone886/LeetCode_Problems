class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [-1] * amount
        n = len(coins)
        
        def helper(total):
            if total == amount:
                return 0
            
            if total > amount:
                return float('inf')
            
            if dp[total] != -1:
                return dp[total]

            min_cnt = float('inf')
            for coin in coins:
                coin_cnt = 1 + helper(total + coin)
                if coin_cnt < min_cnt:
                    min_cnt = coin_cnt
            
            dp[total] = min_cnt
            return dp[total]
        
        ans = helper(0)
        if ans == float('inf'):
            ans = -1
        return ans
        