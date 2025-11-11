# Last updated: 11/11/2025, 5:29:10 AM
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Ai --value[i]--> Bi
        adj = defaultdict(list)

        for i, equation in enumerate(equations):
            adj[equation[0]].append([equation[1], values[i]])
            adj[equation[1]].append([equation[0], 1 / values[i]])

        def dfs(start, end, visited):
            if start == end:
                return 1
            
            visited.add(start)

            for neighbor, value in adj[start]:
                if neighbor in visited:
                    continue
                
                dfs_result = dfs(neighbor, end, visited)
                if dfs_result != 0:
                    return value * dfs_result
                
            return 0

        all_ans = []

        for query in queries:
            numerator = query[0]
            denominator = query[1]

            if numerator not in adj.keys():
                all_ans.append(-1)
            # elif numerator == denominator:
            #     all_ans.append(1)
            else:
                visited = set()
                query_ans = dfs(numerator, denominator, visited)

                if query_ans != 0:
                    all_ans.append(query_ans)
                else:
                    all_ans.append(-1)

        return all_ans