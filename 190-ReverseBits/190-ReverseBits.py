# Last updated: 4/23/2025, 1:51:19 AM
class Solution:
    def reverseBits(self, n: int) -> int:
        mask = 1
        res = 0

        for i in range(31):
            res += mask & n
            res = res << 1
            n = n >> 1
            
        res += mask & n
        return res