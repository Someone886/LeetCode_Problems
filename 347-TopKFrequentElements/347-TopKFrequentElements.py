from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        hash_map = Counter(nums)
        
        return heapq.nlargest(k, hash_map.keys(), key=hash_map.get)