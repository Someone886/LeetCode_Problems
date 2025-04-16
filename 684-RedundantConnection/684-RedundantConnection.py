# Last updated: 4/15/2025, 9:51:40 PM
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # At first, each node's parent is itself
        parents = [i for i in range(len(edges) + 1)]

        # Put the subtree with less nodes to the subtree with more nodes to form a larger subtree
        node_cnts = [1] * (len(edges) + 1)
        
        # To make the tree flat
        def find(n): 
            parent = parents[n]
            # 1. while n -> parent -> parents[parent]
            # 2. then make parent and parents[parent] the same level: 
            #    n -> parent (sibling with) parents[parent] -> parents[parents[parent]]
            # 3. move 1 level up: parent now points to parents[parent]
            # 4. n -> root parent (another node or itself), and return root parent

            while parent != parents[parent]: # 1
                parents[parent] = parents[parents[parent]] # 2
                parent = parents[parent] # 3
            
            # parents[n] = parent

            return parent # 4
        
        def union(n1, n2):
            parent_1, parent_2 = find(n1), find(n2)
            
            # If two nodes point to the same root, then a cycle forms.
            if parent_1 == parent_2:
                return False
            
            # parent with less node cnt -> parent with more node cnt
            # then update node cnt in the bigger subtree
            if node_cnts[parent_1] > node_cnts[parent_2]:
                parents[parent_2] = parent_1
                node_cnts[parent_1] += node_cnts[parent_2]
            
            else:
                parents[parent_1] = parent_2
                node_cnts[parent_2] += node_cnts[parent_1]

            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]