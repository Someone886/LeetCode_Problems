class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if(len(set(nums)) < 3): return False
        t1 = t2 = float("inf")
        for n in nums:
            if n<= t1:
                t1=n
            elif n<=t2:
                t2=n
            else:
                return True
        return False
        