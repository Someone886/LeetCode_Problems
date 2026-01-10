# Last updated: 1/10/2026, 4:51:58 PM
1class Solution:
2    def maxFrequency(self, nums: List[int], k: int) -> int:
3        nums.sort()
4
5        L = 0
6        R = 1
7        total_sum = nums[L]
8        max_freq_cnt = 1
9        n = len(nums)
10
11        while R < n:
12            total_sum += nums[R]
13
14            while nums[R] * (R - L + 1) > total_sum + k:
15                total_sum -= nums[L]
16                L += 1
17            
18            max_freq_cnt = max(max_freq_cnt, R - L + 1)
19            R += 1
20        
21        return max_freq_cnt