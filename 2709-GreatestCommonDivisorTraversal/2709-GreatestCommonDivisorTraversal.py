# Last updated: 11/10/2025, 2:00:03 AM
class Union_Find:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def find(self, node):
        while node != self.parents[node]:
            self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node]
        
        return node
    
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return False

        if self.size[parent1] < self.size[parent2]:
            self.parents[parent1] = parent2
            self.size[parent2] += self.size[parent1]
        
        else:
            self.parents[parent2] = parent1
            self.size[parent1] += self.size[parent2]
        
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # Prime factorization
        # For each num, split it into factors. E.g., 6 -> 1, 2, 3, 6
        # For each factor, map it to num through Union Find. E.g., 3 <-parent- 3 and 3 <-parent- 6

        uf = Union_Find(len(nums))
        # factor_index[f]: index of first num with factor f. 
        # Only keep 1 index in factor_index[f] and use union to add new index to the old union
        factor_index = {} 

        for i, num in enumerate(nums):
            f = 2
            while f * f <= num:
                if num % f == 0:
                    if f in factor_index:
                        uf.union(i, factor_index[f])
                    else:
                        factor_index[f] = i
                
                    while num % f == 0:
                        num = num // f
                f += 1
            
            if num > 1:
                # num is already a factor
                if num in factor_index:
                    uf.union(i, factor_index[num])
                # num is certainly divisible by num itself, so factor_index[num] = i
                else:
                    factor_index[num] = i
        
        return True if max(uf.size) == len(nums) else False
        