# Last updated: 4/12/2025, 1:58:18 AM
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        curr = []
        col_set = set()
        right_top_left_bottom = set() # r + c
        left_top_right_bottom = set() # r - c

        def helper(cnt):
            if cnt == n:
                ans.append(curr.copy())
                return
            
            for col in range(n):
                if col in col_set or \
                    (cnt + col) in right_top_left_bottom or \
                    (cnt - col) in left_top_right_bottom:
                    continue
                
                col_set.add(col)
                right_top_left_bottom.add(cnt + col)
                left_top_right_bottom.add(cnt - col)

                curr.append('.' * col + 'Q' + '.' * (n - 1 - col))
                helper(cnt + 1)
                curr.pop()

                col_set.remove(col)
                right_top_left_bottom.remove(cnt + col)
                left_top_right_bottom.remove(cnt - col)

        
        helper(0)
        return ans