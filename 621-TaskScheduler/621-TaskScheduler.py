# Last updated: 4/8/2025, 9:32:15 PM
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        neg = [-cnt for cnt in counts.values()]
        heapq.heapify(neg)
        pause = deque()
        time = 0

        while neg or pause:
            time += 1
            
            if neg:
                max_count = heapq.heappop(neg)
                max_count += 1
                if max_count < 0:
                    pause.append((max_count, time + n))
            
            else:
                time = pause[0][1]

            while pause and pause[0][1] == time:
                heapq.heappush(neg, pause.popleft()[0])

        return time   