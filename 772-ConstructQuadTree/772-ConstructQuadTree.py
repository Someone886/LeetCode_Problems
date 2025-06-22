# Last updated: 6/22/2025, 2:51:07 PM
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            all_same = True
            default = grid[r][c]
            
            for i in range(n):
                for j in range(n):
                    if grid[r + i][c + j] != default:
                        all_same = False
                        break
            
            if all_same:
                return Node(default, True)

            else:
                new_n = n // 2
                top_left = dfs(new_n, r, c)
                top_right = dfs(new_n, r, c + new_n)
                bottom_left = dfs(new_n, r + new_n, c)
                bottom_right = dfs(new_n, r + new_n, c + new_n)

                return Node(0, False, top_left, top_right, bottom_left, bottom_right)
        
        return dfs(len(grid), 0, 0)