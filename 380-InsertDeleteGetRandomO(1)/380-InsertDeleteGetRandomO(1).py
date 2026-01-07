# Last updated: 1/6/2026, 8:08:53 PM
1import random
2
3class RandomizedSet:
4
5    def __init__(self):
6        # Stores the actual values for random access
7        self.data_list = []
8        # Maps value -> its index in data_list for O(1) lookup
9        self.index_map = {}
10
11    def insert(self, val: int) -> bool:
12        """Inserts a value. Returns False if already present."""
13        if val in self.index_map:
14            return False
15        
16        # Add to the end of the list (O(1))
17        self.data_list.append(val)
18        # Store the index where it was added
19        self.index_map[val] = len(self.data_list) - 1
20        return True
21
22    def remove(self, val: int) -> bool:
23        """Removes a value. Returns False if not present."""
24        if val not in self.index_map:
25            return False
26        
27        # 1. Identify the position of the element to remove
28        idx_to_remove = self.index_map[val]
29        last_element = self.data_list[-1]
30        
31        # 2. Swap the element to remove with the last element
32        # This allows us to pop from the end in O(1) without shifting elements
33        self.data_list[idx_to_remove] = last_element
34        self.index_map[last_element] = idx_to_remove
35        
36        # 3. Clean up: remove the last element from list and the target from map
37        self.data_list.pop()
38        del self.index_map[val]
39        
40        return True
41
42    def getRandom(self) -> int:
43        """Returns a random element from the set in O(1)."""
44        # random.choice works in O(1) on Python lists
45        return random.choice(self.data_list)
46
47
48# Your RandomizedSet object will be instantiated and called as such:
49# obj = RandomizedSet()
50# param_1 = obj.insert(val)
51# param_2 = obj.remove(val)
52# param_3 = obj.getRandom()