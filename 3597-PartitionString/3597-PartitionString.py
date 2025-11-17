# Last updated: 11/17/2025, 2:05:38 AM
class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        curr = ''
        ans = []

        for c in s:
            curr += c
            if curr not in seen:
                ans.append(curr)
                seen.add(curr)
                curr = ''
        
        return ans