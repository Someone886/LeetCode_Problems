# Last updated: 1/12/2026, 3:39:37 PM
1class TimeMap:
2
3    def __init__(self):
4        self.value_map = defaultdict(list)
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        self.value_map[key].append([value, timestamp])
8
9    def get(self, key: str, timestamp: int) -> str:
10        if key not in self.value_map:
11            return ""
12        
13        values = self.value_map[key]
14        l, r = 0, len(values) - 1
15        res = "" # Initialize as empty string
16
17        while l <= r:
18            mid = (l + r) // 2
19            
20            # If current mid is less than or equal to target
21            if values[mid][1] <= timestamp:
22                res = values[mid][0]  # This is a valid candidate
23                l = mid + 1           # Try to find something even closer/larger
24            else:
25                # This timestamp is too large, look left
26                r = mid - 1
27        
28        return res
29
30# Your TimeMap object will be instantiated and called as such:
31# obj = TimeMap()
32# obj.set(key,value,timestamp)
33# param_2 = obj.get(key,timestamp)