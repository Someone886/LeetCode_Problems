# Last updated: 6/22/2025, 2:52:24 PM
class Node:
    def __init__(self, val=-1, prev = None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.value_map = {}
        self.node_map = {}

        self.capacity = capacity
        self.dummy_head = Node()
        self.dummy_tail = Node()

        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        if key in self.value_map:
            val = self.value_map[key]
            node = self.node_map[key]

            node.prev.next, node.next.prev = node.next, node.prev

            self.dummy_tail.prev.next = node
            node.next = self.dummy_tail
            node.prev = self.dummy_tail.prev
            self.dummy_tail.prev = node

            return val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.value_map:
            self.value_map[key] = value

            node = self.node_map[key]
            node.prev.next, node.next.prev = node.next, node.prev

            self.dummy_tail.prev.next = node
            node.next = self.dummy_tail
            node.prev = self.dummy_tail.prev
            self.dummy_tail.prev = node

        else:
            if self.capacity > 0:
                self.capacity -= 1

                node = Node(key)
                self.value_map[key] = value
                self.node_map[key] = node

                self.dummy_tail.prev.next = node
                node.next = self.dummy_tail
                node.prev = self.dummy_tail.prev
                self.dummy_tail.prev = node
            
            else:
                node = self.dummy_head.next
                original_key = node.val
                self.value_map.pop(original_key)
                self.node_map.pop(original_key)

                node.val = key

                self.value_map[key] = value
                self.node_map[key] = node

                node.prev.next, node.next.prev = node.next, node.prev

                self.dummy_tail.prev.next = node
                node.next = self.dummy_tail
                node.prev = self.dummy_tail.prev
                self.dummy_tail.prev = node