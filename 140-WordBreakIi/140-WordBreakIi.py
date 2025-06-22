# Last updated: 6/22/2025, 2:52:27 PM
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        curr = []

        def dfs(start):
            if start == len(s):
                ans.append(" ".join(curr))
                return
            
            for i in range(start + 1, len(s) + 1):
                if s[start:i] in wordDict:
                    curr.append(s[start:i])
                    dfs(i)
                    curr.pop()
        
        dfs(0)
        return ans
