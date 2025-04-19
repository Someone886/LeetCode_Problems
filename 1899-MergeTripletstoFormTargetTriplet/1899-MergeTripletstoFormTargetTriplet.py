# Last updated: 4/19/2025, 1:00:59 AM
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = False, False, False

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            if triplet[0] == target[0]:
                a = True
            
            if triplet[1] == target[1]:
                b = True

            if triplet[2] == target[2]:
                c = True
            
            if a and b and c:
                return True
        
        return False