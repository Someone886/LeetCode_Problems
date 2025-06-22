# Last updated: 6/22/2025, 2:51:15 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map = Counter(s1)
        init_map = Counter(s2[0:len(s1)])

        if freq_map == init_map:
            return True

        for r in range(len(s1), len(s2)):
            l = r - len(s1)

            init_map[s2[l]] -= 1
            init_map[s2[r]] += 1

            if s2[r] in freq_map:
                if freq_map == init_map:
                    return True
        
        return False