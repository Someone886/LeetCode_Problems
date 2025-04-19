# Last updated: 4/19/2025, 4:51:00 PM
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_column_zero = False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if j == 0:
                        first_column_zero = True
                        matrix[i][0] = 0
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
        
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
        
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(1, len(matrix)):
                    matrix[j][i] = 0
        
        if matrix[0][0] == 0:
            for i in range(0, len(matrix[0])):
                matrix[0][i] = 0
        
        if first_column_zero:
            for i in range(0, len(matrix)):
                matrix[i][0] = 0