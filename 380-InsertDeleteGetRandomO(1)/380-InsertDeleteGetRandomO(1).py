// Last updated: 3/20/2025, 9:48:38 PM
class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.items = []

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
        else:
            self.items.append(val)
            self.hash_map[val] = len(self.items) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map:
            return False
        else:
            position = self.hash_map.pop(val)
            last_item = self.items.pop()
            if last_item != val:
                self.items[position] = last_item
                self.hash_map[last_item] = position
            return True

    def getRandom(self) -> int:
        return random.choice(self.items)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()