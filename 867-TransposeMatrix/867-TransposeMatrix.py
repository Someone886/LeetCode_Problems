# Last updated: 5/18/2025, 3:00:26 AM
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]