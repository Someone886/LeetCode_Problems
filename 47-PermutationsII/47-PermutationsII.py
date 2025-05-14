# Last updated: 5/13/2025, 10:46:47 PM
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        hash_map = Counter(nums)
        ans = []
        curr = []

        def dfs():
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return
            
            for n in hash_map:
                if hash_map[n] > 0:
                    curr.append(n)
                    hash_map[n] -= 1
                    dfs()
                    curr.pop()
                    hash_map[n] += 1
        
        dfs()
        return ans
