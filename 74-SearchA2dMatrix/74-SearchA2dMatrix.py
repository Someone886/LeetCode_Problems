# Last updated: 6/22/2025, 2:53:12 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            middle = (left + right)//2
            row = middle // n
            col = middle % n
            curr = matrix[row][col]
            
            if curr == target:
                return True
            
            elif curr > target:
                right = middle - 1
            
            else:
                left = middle + 1
        
        return False