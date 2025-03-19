import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickselect(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []
            for n in nums:
                if n > pivot:
                    left.append(n)
                elif n < pivot:
                    right.append(n)
                else:
                    mid.append(n)
            
            if len(left) >= k:
                return quickselect(left, k)
            elif len(left) + len(mid) < k:
                return quickselect(right, k - len(left) - len(mid))
            else:
                return pivot
        
        return quickselect(nums, k)