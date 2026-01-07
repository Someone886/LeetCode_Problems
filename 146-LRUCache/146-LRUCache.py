# Last updated: 1/6/2026, 7:59:16 PM
1class Node:
2    def __init__(self, key=-1, val=-1):
3        self.key = key  # We store key to remove it from the dict during eviction
4        self.val = val
5        self.prev = None
6        self.next = None
7
8class LRUCache:
9    def __init__(self, capacity: int):
10        self.capacity = capacity
11        # We only need one map: key -> Node object (which stores the value)
12        self.cache = {} 
13        
14        # Sentinel nodes to avoid null checks during insertion/deletion
15        self.head = Node()
16        self.tail = Node()
17        self.head.next = self.tail
18        self.tail.prev = self.head
19
20    def _remove(self, node: Node):
21        """Unlinks a node from its current position in the list."""
22        prev_node = node.prev
23        next_node = node.next
24        prev_node.next = next_node
25        next_node.prev = prev_node
26
27    def _add_to_tail(self, node: Node):
28        """Always inserts the node right before the dummy tail (Most Recently Used)."""
29        last_real_node = self.tail.prev
30        
31        last_real_node.next = node
32        node.prev = last_real_node
33        node.next = self.tail
34        self.tail.prev = node
35
36    def get(self, key: int) -> int:
37        if key in self.cache:
38            node = self.cache[key]
39            # Since we accessed it, move it to the tail (MRU)
40            self._remove(node)
41            self._add_to_tail(node)
42            return node.val
43        return -1
44
45    def put(self, key: int, value: int) -> None:
46        if key in self.cache:
47            # Update existing value and move to tail
48            node = self.cache[key]
49            node.val = value
50            self._remove(node)
51            self._add_to_tail(node)
52        else:
53            if len(self.cache) >= self.capacity:
54                # 1. Identify the Least Recently Used (node after dummy head)
55                lru_node = self.head.next
56                # 2. Remove it from the list
57                self._remove(lru_node)
58                # 3. Evict it from the dictionary
59                del self.cache[lru_node.key]
60
61            # Create new node and add to tail
62            new_node = Node(key, value)
63            self.cache[key] = new_node
64            self._add_to_tail(new_node)