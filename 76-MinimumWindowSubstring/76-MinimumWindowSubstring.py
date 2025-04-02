# Last updated: 4/1/2025, 10:20:19 PM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        t_map = Counter(t)
        need = len(t_map.keys())
        seen = 0

        window_map = {}
        
        min_size = len(s) + 1
        min_range = [-1, -1]

        l = 0
        for r in range(0, len(s)):
            window_map[s[r]] = 1 + window_map.get(s[r], 0)

            if s[r] in t_map:
                if window_map[s[r]] == t_map[s[r]]:
                    seen += 1
                
                while seen == need:
                    if r - l + 1 < min_size:
                        min_size = r - l + 1
                        min_range = [l, r + 1]

                    window_map[s[l]] -= 1
                    if s[l] in t_map and window_map[s[l]] < t_map[s[l]]:
                        seen -= 1
                        
                    l += 1
                
        return s[min_range[0]:min_range[1]]