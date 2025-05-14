# Last updated: 5/13/2025, 11:58:32 PM
class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        col_set = set()
        right_top_left_bottom = set() # r + c
        left_top_right_bottom = set() # r - c

        def helper(cnt):
            nonlocal ans
            
            if cnt == n:
                ans += 1
                return
            
            for col in range(n):
                if col in col_set or \
                    (cnt + col) in right_top_left_bottom or \
                    (cnt - col) in left_top_right_bottom:
                    continue
                
                col_set.add(col)
                right_top_left_bottom.add(cnt + col)
                left_top_right_bottom.add(cnt - col)

                helper(cnt + 1)

                col_set.remove(col)
                right_top_left_bottom.remove(cnt + col)
                left_top_right_bottom.remove(cnt - col)

        
        helper(0)
        return ans