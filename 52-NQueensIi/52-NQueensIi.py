# Last updated: 6/22/2025, 2:53:20 PM
class Solution:
    def totalNQueens(self, n: int) -> int:
        memo = {}  # For memoization

        def solve(r, col_mask, diag1_mask, diag2_mask):
            """
            Calculates the number of ways to place N queens from row 'r' onwards.
            
            r: current row to place a queen (0 to n-1)
            col_mask: bitmask of occupied columns
            diag1_mask: bitmask of occupied diagonals (r + c)
            diag2_mask: bitmask of occupied diagonals (r - c + n - 1)
            """
            # Base case: If all queens are placed (current row is n)
            if r == n:
                return 1  # Found one valid placement

            # Memoization check
            state = (r, col_mask, diag1_mask, diag2_mask)
            if state in memo:
                return memo[state]

            count = 0
            # Try placing a queen in each column 'c' of the current row 'r'
            for c in range(n):
                # Check if column 'c' is available
                is_col_safe = not (col_mask & (1 << c))
                
                # Check if diagonal (r + c) is available
                diag1_val = r + c
                is_diag1_safe = not (diag1_mask & (1 << diag1_val))
                
                # Check if diagonal (r - c + n - 1) is available
                # (r - c) can be negative. Adjust by (n-1) to be non-negative for bitmask index.
                # Range of r-c is -(n-1) to (n-1).
                # Shifted range r-c+(n-1) is 0 to 2n-2.
                diag2_val = r - c + (n - 1)
                is_diag2_safe = not (diag2_mask & (1 << diag2_val))

                if is_col_safe and is_diag1_safe and is_diag2_safe:
                    # Place queen and recurse for the next row
                    new_col_mask = col_mask | (1 << c)
                    new_diag1_mask = diag1_mask | (1 << diag1_val)
                    new_diag2_mask = diag2_mask | (1 << diag2_val)
                    
                    count += solve(r + 1, new_col_mask, new_diag1_mask, new_diag2_mask)
            
            # Store result in memo before returning
            memo[state] = count
            return count

        # Initial call: start at row 0 with all masks empty (0)
        return solve(0, 0, 0, 0)