# Last updated: 6/22/2025, 2:58:53 PM
class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        r = 0
        c = n - 1

        while c >= 0 and r <= m-1:
            if matrix[r][c] == target:
                # found
                return True
            if matrix[r][c] > target:
                # current larger than target, 
                # then target must be on the left / left-bottom side of current
                c -= 1
            else:
                # current smaller than target,
                # then targer must be below current.
                # Could be just below it, or left-below it.
                r += 1
        
        return False