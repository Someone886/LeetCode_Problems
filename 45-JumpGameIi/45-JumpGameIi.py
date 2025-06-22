# Last updated: 6/22/2025, 2:53:24 PM
class Solution:
    def jump(self, nums: List[int]) -> int:
        cnt = 0
        l, r = 0, 0
        # l, r tracks the range that can be reached with exactly "cnt" jumps ~ BFS

        while r < len(nums) - 1:
            far_reach = l
            for i in range(l, r + 1):
                far_reach = max(far_reach, i + nums[i])
            
            l = r + 1
            r = far_reach
            cnt += 1
        
        return cnt