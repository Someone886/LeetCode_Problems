class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n * (n + 1) / 2 + n * (n - 1) + (n - 1) * (n - 2) / 2