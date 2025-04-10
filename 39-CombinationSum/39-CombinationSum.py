# Last updated: 4/10/2025, 7:33:16 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        comb = []

        def helper(index, sum_so_far):
            if sum_so_far > target:
                return
            
            if sum_so_far == target:
                ans.append(comb.copy())
                return
            
            for i in range(index, len(candidates)):
                comb.append(candidates[i])
                helper(i, sum_so_far + candidates[i])
                comb.pop()
        
        helper(0, 0)
        return ans