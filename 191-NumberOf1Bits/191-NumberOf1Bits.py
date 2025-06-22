# Last updated: 6/22/2025, 2:52:18 PM
class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        cnt = 0

        for i in range(32):
            cnt += mask & (n >> i) 
        
        return cnt