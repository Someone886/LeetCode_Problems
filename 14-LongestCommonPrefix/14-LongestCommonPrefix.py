# Last updated: 4/26/2025, 3:05:28 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        ans = ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for string in strs[1:]:
                if len(string) < i + 1:
                    return ans
                elif string[i] == char:
                    continue
                else:
                    return ans
            ans += char
        return ans