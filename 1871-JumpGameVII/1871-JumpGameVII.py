# Last updated: 11/13/2025, 3:51:25 AM
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # BFS + keep track of farthest
        q = deque([0])
        farthest = 0
        n = len(s)

        while q:
            curr_index = q.popleft()
            next_index_start = max(curr_index + minJump, farthest + 1)
            
            for next_index in range(next_index_start, min(curr_index + maxJump + 1, n)):
                if s[next_index] == '0':
                    if next_index == n - 1:
                        return True
                    else:
                        q.append(next_index)
            
            farthest = curr_index + maxJump
        
        return False
        