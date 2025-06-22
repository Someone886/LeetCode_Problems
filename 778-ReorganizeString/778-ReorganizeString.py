# Last updated: 6/22/2025, 2:51:06 PM
class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counts = Counter(s)
        max_heap = []
        heapq.heapify(max_heap)
        ans = ""

        for value, freq in counts.items():
            if freq > (n + 1) // 2:
                return ""
            heapq.heappush(max_heap, (-freq, value))
        
        ans = ""
        while len(max_heap) >= 2:
            # take the two most frequent
            f1, ch1 = heapq.heappop(max_heap)
            f2, ch2 = heapq.heappop(max_heap)

            ans += ch1
            ans += ch2

            # decrement counts (remember f1,f2 are negative)
            if f1 + 1 < 0:
                heapq.heappush(max_heap, (f1 + 1, ch1))
            if f2 + 1 < 0:
                heapq.heappush(max_heap, (f2 + 1, ch2))

        # if one remains, append it
        if max_heap:
            ans += max_heap[0][1]

        return ans