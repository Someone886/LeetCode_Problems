# Last updated: 4/9/2025, 4:46:48 AM
class WordDictionary:

    def __init__(self):
        self.hash_map = {}

    def addWord(self, word: str) -> None:
        node = self.hash_map
        
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        
        node[None] = None

    def search(self, word: str) -> bool:
        
        def dfs(j, curr_node):
            if curr_node == None:
                return False

            if j == len(word):
                if None in curr_node:
                    return True
                else:
                    return False
            
            char = word[j]
            if char != '.':
                if char not in curr_node:
                    return False
                else:
                    return dfs(j+1, curr_node[char])
            else:
                for child_node in curr_node.values():
                    if dfs(j + 1, child_node):
                        return True
                return False
        
        return dfs(0, self.hash_map)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)