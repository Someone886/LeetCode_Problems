class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        first_row = 1
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        first_row = 0
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                matrix[i] = [0] * n
        
        for j in range(0, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        if first_row == 0:
            matrix[0] = [0] * n