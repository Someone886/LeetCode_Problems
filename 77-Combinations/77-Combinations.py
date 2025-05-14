# Last updated: 5/13/2025, 10:24:56 PM
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        curr = []
        
        def dfs(index):
            if len(curr) == k:
                ans.append(curr.copy())
                return
            
            for i in range(index + 1, n + 1):
                curr.append(i)
                dfs(i)
                curr.pop()
        
        dfs(0)
        return ans