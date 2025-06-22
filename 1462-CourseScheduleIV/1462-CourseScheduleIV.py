class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)

        # Build graph: pre → course
        for pre, course in prerequisites:
            graph[pre].append(course)

        @cache
        def dfs(course: int) -> set:
            reachable = set()
            for neighbor in graph[course]:
                reachable |= dfs(neighbor)
                reachable.add(neighbor)
            return reachable

        result = []
        for u, v in queries:
            result.append(v in dfs(u))

        return result


'''
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        memo = {}
        
        # Build graph: course A → course B means A is a prerequisite of B
        for pre, course in prerequisites:
            graph[pre].append(course)

        def dfs(start, target):
            if (start, target) in memo:
                return memo[(start, target)]

            if start == target:
                memo[(start, target)] = True
                return True

            for neighbor in graph[start]:
                if dfs(neighbor, target):
                    memo[(start, target)] = True
                    return True

            memo[(start, target)] = False
            return False

        result = []
        for u, v in queries:
            # Note: u cannot be a prerequisite of itself unless explicitly in the graph
            if u == v:
                result.append(False)
            else:
                result.append(dfs(u, v))

        return result
'''

