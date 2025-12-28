# Last updated: 12/28/2025, 12:14:44 AM
1class TrieNode:
2    def __init__(self):
3        self.children = {}
4        self.is_end = False
5
6class Trie:
7    def __init__(self):
8        self.root = TrieNode()
9
10    def insert(self, word: str) -> None:
11        node = self.root
12        for char in word:
13            if char not in node.children:
14                node.children[char] = TrieNode()
15            node = node.children[char]
16        node.is_end = True
17
18class Solution:
19    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
20        trie = Trie()
21        for word in dictionary:
22            trie.insert(word)
23        
24        sentence_words = sentence.split(" ")
25        ans = []
26
27        def find_shortest_root(word):
28            node = trie.root
29            shortest_replacement = ""
30            for char in word:
31                if char in node.children:
32                    node = node.children[char]
33                    shortest_replacement += char
34                    if node.is_end:
35                        return shortest_replacement
36                else:
37                    break
38
39            return word
40
41
42        for sentence_word in sentence_words:
43            ans.append(find_shortest_root(sentence_word))
44        
45        return " ".join(ans)