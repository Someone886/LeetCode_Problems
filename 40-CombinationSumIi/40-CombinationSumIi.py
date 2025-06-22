# Last updated: 6/22/2025, 2:53:28 PM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        comb = []
        candidates.sort()

        def helper(index, sum_so_far):
            if sum_so_far > target:
                return
            
            if sum_so_far == target:
                ans.append(comb.copy())
                return
            
            for i in range(index + 1, len(candidates)):
                if i > index + 1 and candidates[i] == candidates[i - 1]:
                    continue
                comb.append(candidates[i])
                helper(i, sum_so_far + candidates[i])
                comb.pop()
        
        helper(-1, 0)
        return ans