# Last updated: 5/4/2025, 2:27:56 AM
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = min_sum = max(nums)
        r = max_sum = sum(nums)

        def fit_in(target_sum):
            group = 1
            curr_sum = 0
            
            for num in nums:
                if curr_sum + num > target_sum:
                    group += 1
                    if group > k:
                        return False
                    curr_sum = 0
                curr_sum += num
            
            return True

        while l <= r:
            m = (l + r) // 2

            if fit_in(m):
                r = m - 1
            else:
                l = m + 1
        
        return l


'''
    def splitArray(self, nums: List[int], k: int) -> int:
        dp = {}

        # ith index starts a new group, with m groups left
        def helper(i, m):
            if m == 1:
                return sum(nums[i:])
            
            if (i, m) in dp:
                return dp[(i, m)]
            
            min_sum = float('inf')
            curr_sum = 0
            for next_cut in range(i + 1, len(nums) - m + 2):
                curr_sum += nums[next_cut - 1]
                max_tail = max(curr_sum, helper(next_cut, m - 1))
                min_sum = min(min_sum, max_tail)
                if curr_sum > min_sum:
                    break
            
            dp[(i, m)] = min_sum
            return min_sum
        
        return helper(0, k)
'''