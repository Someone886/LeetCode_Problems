# Last updated: 6/22/2025, 2:50:35 PM
class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 1 + n*(n-1)*2