from bisect import bisect_left

class Solution(object):
    def lengthOfLIS(self, nums):
        dp = []

        for i, num in enumerate(nums):
            index = bisect_left(dp, num)
            n = len(dp)

            if index == n:
                dp.append(num)
            else:
                dp[index] = num
        
        return len(dp)

'''
This implementation leverages the Patience Sorting idea to compute the length of the longest strictly increasing subsequence in O(n log n) time:

- dp as a “tails” array
We maintain a list dp where dp[i] is the smallest possible tail value of any increasing subsequence of length i + 1 seen so far. Keeping these tails as small as possible maximizes the chance to extend them with future numbers.

- Finding the insertion point with bisect_left
Each time we see a new number num, we call

index = bisect_left(dp, num)

This returns the leftmost position in the sorted list dp where num can be inserted so that dp remains sorted. In other words, it finds the first dp[index] ≥ num in O(log n) time.

- Extending vs. updating

if index == len(dp):
    dp.append(num)
else:
    dp[index] = num
If index equals the current length of dp, num is larger than all existing tails, so we extend our longest subsequence by appending it.

Otherwise, we replace dp[index] with num, lowering the tail for subsequences of length index+1 and improving the chance of future extensions.

- Final answer
After processing every element, the length of dp is exactly the length of the longest strictly increasing subsequence in nums.
'''
