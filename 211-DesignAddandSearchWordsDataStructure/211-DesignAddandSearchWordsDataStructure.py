# Last updated: 11/16/2025, 6:14:17 AM
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(child, sub_word):

            curr = child

            for i in range(len(sub_word)):
                c = sub_word[i]
                if c != '.':
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
                else:
                    for child in curr.children.values():
                        if dfs(child, sub_word[i+1:]):
                            return True
                    
                    return False
            
            return curr.end

        
        return dfs(self.root, word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)