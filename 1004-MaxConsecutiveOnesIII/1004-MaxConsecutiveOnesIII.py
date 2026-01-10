# Last updated: 1/10/2026, 1:40:20 PM
1class Solution:
2    def longestOnes(self, nums: List[int], k: int) -> int:
3        left = 0
4        right = 0
5        zero_counts = 0
6        n = len(nums)
7        max_length = right - left
8
9        while right < n:
10            if nums[right] == 1:
11                right += 1
12                max_length = max(max_length, right - left)
13                
14            else:
15                zero_counts += 1
16                right += 1
17
18                if zero_counts > k:
19                    while nums[left] != 0:
20                        left += 1
21                    left += 1
22                    zero_counts -= 1
23                
24                max_length = max(max_length, right - left)
25        
26        return max_length