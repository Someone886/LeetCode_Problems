# Last updated: 6/22/2025, 2:50:48 PM
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        mountain_length = mountainArr.length()

        # peak never at boundary + if set to 0 and length - 1, index out of bound at the boundary
        l = 1
        r = mountain_length - 2
        
        while l <= r:
            m = (l + r) // 2
            left, middle, right = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)

            if left < middle < right:
                l = m + 1
            
            elif left > middle > right:
                r = m - 1

            else:
                break
        
        peak = m

        # search left
        l = 0
        r = peak
        
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)

            if val == target:
                return m
            
            elif val > target:
                r = m - 1
            
            else:
                l = m + 1
        
        # search right
        l = peak
        r = mountain_length - 1

        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)

            if val == target:
                return m
            
            elif val < target:
                r = m - 1
            
            else:
                l = m + 1
        
        return -1
