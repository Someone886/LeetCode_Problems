# Last updated: 11/13/2025, 12:57:03 AM
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Iterate value by value, keep track of curr max so far, including curr value
        # Then update global max using the curr max

        # curr_max initialized to 0
        # global_max initalized to any value in the array

        # curr_max = max(prev curr_max + curr, curr)

        # Note that: if A is a max array, then N - A is a min array
        # -> keep track of curr_min and global_min

        # -> ans = max(global_max, total - global_min)

        all_sum = 0
        n = len(nums)

        curr_max, curr_min = float('-inf'), float('inf')
        global_max, global_min = nums[0], nums[0]

        for i in range(n):
            curr_max = max(nums[i], curr_max + nums[i])
            global_max = max(global_max, curr_max)

            curr_min = min(nums[i], curr_min + nums[i])
            global_min = min(global_min, curr_min)

            all_sum += nums[i]

        # if global_max < 0, then all negative nums -> all_sum - global_min = 0 
        # -> return global_max instead
        return max(global_max, all_sum - global_min) if global_max > 0 else global_max 