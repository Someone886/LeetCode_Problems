# Last updated: 4/19/2025, 1:30:02 AM
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i
        
        l = r = 0
        ans = []
        size = 1

        while l < len(s):
            char = s[l]
            r = last_index[char]
            size = 1

            while l < r:
                l += 1
                r = max(last_index[s[l]], r)

                size += 1
            
            ans.append(size)
            l = r + 1
        
        return ans