# Last updated: 4/9/2025, 3:59:20 AM
class Trie:

    def __init__(self):
        self.hash_map = {}

    def insert(self, word: str) -> None:
        node = self.hash_map
        for char in word:
            if char in node:
                node = node[char]
            else:
                node[char] = {}
                node = node[char]

        node[None] = True
        # print(self.hash_map)

    def search(self, word: str) -> bool:
        node = self.hash_map
        for char in word:
            if char not in node:
                return False
            node = node[char]
        
        if None in node:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        node = self.hash_map
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)