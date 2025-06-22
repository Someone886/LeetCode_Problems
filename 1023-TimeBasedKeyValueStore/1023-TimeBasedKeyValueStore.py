# Last updated: 6/22/2025, 2:50:53 PM
from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.value_map = defaultdict(list)
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.value_map[key].append(value)
        self.time_map[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.value_map:
            return ""
        
        value_bucket = self.value_map[key]
        time_bucket = self.time_map[key]

        l, r = 0, len(time_bucket) - 1
        res = -1

        while l <= r:
            middle = (l + r) // 2

            if time_bucket[middle] == timestamp:
                res = middle
                break
            
            elif time_bucket[middle] > timestamp:
                r = middle - 1
            
            else:
                res = middle
                l = middle + 1
        
        if res == -1:
            return ""
        
        return value_bucket[res]