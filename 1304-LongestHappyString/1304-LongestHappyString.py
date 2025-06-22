# Last updated: 6/22/2025, 2:50:45 PM
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        q = []
        heapq.heapify(q)
        ans = ""
        
        if a > 0:
            heapq.heappush(q, (-a, "a"))
        if b > 0:
            heapq.heappush(q, (-b, "b"))
        if c > 0:
            heapq.heappush(q, (-c, "c"))

        last_third, last_second = None, None

        while q:
            neg_freq, next_char = heapq.heappop(q)
            if last_third == last_second and last_second == next_char:
                if not q:
                    return ans
                else:
                    neg_freq_2, next_char_2 = heapq.heappop(q)
                    heapq.heappush(q, (neg_freq, next_char))

                    last_third, last_second = last_second, next_char_2
                    ans += next_char_2

                    if neg_freq_2 + 1 != 0:
                        heapq.heappush(q, (neg_freq_2 + 1, next_char_2))
            else:
                last_third, last_second = last_second, next_char
                ans += next_char

                if neg_freq + 1 != 0:
                    heapq.heappush(q, (neg_freq + 1, next_char))
        
        return ans
