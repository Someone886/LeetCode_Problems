# Last updated: 4/19/2025, 3:14:15 PM
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res = []

        while l < r and top < bottom:
            for i in range(l, r):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][r - 1])
            r -= 1
            
            if not (l < r and top < bottom):
                break

            for i in range(r - 1, l - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][l])
            l += 1

        return res