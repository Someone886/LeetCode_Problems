# Last updated: 4/15/2025, 8:47:09 AM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list)

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        
        already_visited = {}
        # if crs: false, then its prerequisites are being visited in this batch -> if seen again, then a loop
        # if crs: true, then its already visited and processed -> if seen again, then landed at a safe node

        def dfs(crs):
            if crs in already_visited:
                return already_visited[crs]
            
            already_visited[crs] = False

            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False

            already_visited[crs] = True

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
        