# Last updated: 6/22/2025, 2:50:43 PM
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [-1] * n

        def dfs(index):
            if index == n:
                return 0
            
            if dp[index] != -1:
                return dp[index]
            
            res = float("-inf")
            picked_sum = 0
            for i in range(index, index + 3):
                if i >= n:
                    break
                picked_sum += stoneValue[i]
                res = max(res, picked_sum - dfs(i + 1))
            dp[index] = res
            return res
        
        ans = dfs(0)
        if ans > 0:
            return "Alice"
        elif ans == 0:
            return "Tie"
        else:
            return "Bob"
            
'''
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}
        n = len(stoneValue)

        def helper(index, person):
            if index == n:
                return 0
            
            if (index, person) in dp:
                return dp[(index, person)]

            min_max_score = float('-inf')
            pick_sum = 0
            for i in range(index, min(index + 3, n)):
                pick_sum += stoneValue[i]
                min_max_score = max(min_max_score, pick_sum - helper(i + 1, -person))
            dp[(index, person)] = min_max_score

            return min_max_score
        
        ans = helper(0, 1)
        
        if ans > 0:
            return "Alice"
        elif ans == 0:
            return "Tie"
        else:
            return "Bob"
'''