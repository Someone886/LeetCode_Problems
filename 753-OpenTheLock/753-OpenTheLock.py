# Last updated: 6/22/2025, 2:51:08 PM
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        def children(lock):
            res = []

            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])

                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            
            return res
        
        visited = set(deadends)

        visiting = deque(["0000"])
        steps = 0

        while visiting:
            for _ in range(len(visiting)):
                comb = visiting.popleft()

                if comb == target:
                    return steps
                
                if comb in visited:
                    continue
                
                visited.add(comb)

                for child in children(comb):
                    if child not in visited:
                        visiting.append(child)
            
            steps += 1

        return -1