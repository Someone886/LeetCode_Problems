# Last updated: 11/16/2025, 5:42:51 AM
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        i = 0
        n = len(word)

        while i < n:
            if word[i] in curr.children:
                curr = curr.children[word[i]]
            else:
                curr.children[word[i]] = TrieNode()
                curr = curr.children[word[i]]
            i += 1

        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        i = 0
        n = len(word)

        while i < n:
            if word[i] in curr.children:
                curr = curr.children[word[i]]
            else:
                return False
            i += 1
        
        if curr.end:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        i = 0
        n = len(prefix)

        while i < n:
            if prefix[i] in curr.children:
                curr = curr.children[prefix[i]]
            else:
                return False
            i += 1
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)