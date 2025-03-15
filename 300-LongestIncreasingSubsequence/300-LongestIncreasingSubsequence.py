from bisect import bisect_left

class Solution(object):
    def lengthOfLIS(self, nums):
        dp = []

        for i, num in enumerate(nums):
            index = bisect_left(dp, num)
            n = len(dp)

            if index > n - 1:
                dp.append(num)
            else:
                dp[index] = num
        
        return len(dp)