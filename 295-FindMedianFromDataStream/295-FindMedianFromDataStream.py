# Last updated: 6/22/2025, 2:51:35 PM
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.min_heap and not self.max_heap:
            heapq.heappush(self.min_heap, num)
            return

        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -num)

        # len(self.max_heap) >= len(self.min_heap)
        else:
            heapq.heappush(self.min_heap, num)

        # rebalance so that max of max_heap < min of min_heap
        while -self.max_heap[0] > self.min_heap[0]:
            max_of_max = heapq.heappushpop(self.max_heap, -heapq.heappop(self.min_heap))
            heapq.heappush(self.min_heap, -max_of_max)

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()