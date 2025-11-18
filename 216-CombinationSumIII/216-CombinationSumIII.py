# Last updated: 11/17/2025, 10:43:18 PM
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = []
        curr = []

        def find(start_number, curr_sum):
            if len(curr) == k:
                if curr_sum == n:
                    output.append(curr.copy())
                return
            
            for next_number in range(start_number + 1, 10):
                if curr_sum + next_number > n:
                    break
                
                curr.append(next_number)
                find(next_number, curr_sum + next_number)
                curr.pop()
            
        find(0, 0)
        
        return output