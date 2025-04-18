# Last updated: 4/18/2025, 7:57:03 PM
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hash_map = Counter(hand)
        keys = list(hash_map.keys())
        heapq.heapify(keys)

        while keys:
            start = keys[0]

            for i in range(groupSize):
                if start + i not in hash_map or hash_map[start + i] == 0:
                    return False
                
                hash_map[start + i] -= 1
            
            while keys and hash_map[keys[0]] == 0:
                heapq.heappop(keys)
        
        return True