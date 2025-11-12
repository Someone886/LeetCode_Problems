# Last updated: 11/12/2025, 3:14:53 AM
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # Constructing the n-th number by:
        # 1. Starting from x
        # 2. Inserting bits of (n-1) into the zero bits of x (from right to left)
        # That’s because only those 0-bits can change while keeping num & x == x.

        res = x
        i_x = 1 # mask for ith bit of x
        i_n = 1 # mask for ith bit of n

        while i_n <= n - 1: 

            # if ith bit of x is 0, candidate for inserting 1
            if i_x & x == 0: 

                # "if i_n & (n - 1) != 0": how it "inserts" the binary digits of (n-1) 
                #   into the available 0-bits of x:
                # If a bit in (n-1) is 1, set that position in res.
                # If it’s 0, leave it as is.
                # Analogy:
                # - (n-1) as a blueprint showing which “holes” (zero bits in x) to fill.
                # - i_n as a scanner that moves through each possible hole.
                # - if i_n & (n - 1) asks: "Does this hole get filled (bit = 1) or not (bit = 0)?"
                if i_n & (n - 1) != 0:
                    res = res | i_x # set ith bit to be 1 in res

                i_n = i_n << 1
            i_x = i_x << 1
        
        return res 