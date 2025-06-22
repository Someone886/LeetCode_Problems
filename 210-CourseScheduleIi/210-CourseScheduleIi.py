# Last updated: 6/22/2025, 2:52:14 PM
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = defaultdict(list)

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        

        order = []
        visited = {}

        def dfs(crs):
            if crs in visited:
                return visited[crs]
            
            visited[crs] = False
            for next_crs in pre_map[crs]:
                if not dfs(next_crs):
                    return False
            
            order.append(crs)
            visited[crs] = True
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return order
        