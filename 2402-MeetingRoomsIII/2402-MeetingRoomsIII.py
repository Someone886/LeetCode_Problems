# Last updated: 6/3/2025, 12:45:33 AM
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = [i for i in range(n)]
        used = [] # storing (end_time, room_number)
        cnt = [0] * n

        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room_num = heappop(used)
                heappush(available, room_num)
            
            if not available:
                earlist_end, room_num = heappop(used)
                duration = end - start
                heappush(used, (earlist_end + duration, room_num))
                cnt[room_num] += 1

            else:
                smallest_available = heappop(available)
                heappush(used, (end, smallest_available))
                cnt[smallest_available] += 1

        return cnt.index(max(cnt))
