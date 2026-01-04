# Last updated: 1/3/2026, 8:23:14 PM
1from collections import defaultdict, deque
2
3class Solution:
4    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
5        # Edge case: If the destination isn't in the list, no path is possible
6        if endWord not in wordList:
7            return 0
8        
9        # neighbors maps intermediate patterns to actual words
10        # Example: "h*t" -> ["hot", "hit", "hat"]
11        neighbors = defaultdict(list)
12        wordList.append(beginWord)
13
14        # PREPROCESSING: Build the adjacency list using patterns
15        for word in wordList:
16            for j in range(len(word)):
17                # Replace each character with a wildcard to create a pattern
18                pattern = word[:j] + "*" + word[j + 1:]
19                neighbors[pattern].append(word)
20        
21        # BFS SETUP
22        visited = set([beginWord]) # Track visited words to avoid infinite loops
23        q = deque([beginWord])     # Queue for level-order traversal
24        diff = 1                   # Represents the number of words in the current path
25
26        while q:
27            # Process all nodes currently in the queue (the current 'level')
28            for i in range(len(q)):
29                next_word = q.popleft()
30
31                # For the current word, generate all possible patterns it could fit
32                for j in range(len(next_word)):
33                    pattern = next_word[:j] + "*" + next_word[j + 1:]
34
35                    # Check every word that matches this wildcard pattern
36                    for neighbor in neighbors[pattern]:
37                        # Success condition: reached the target
38                        if neighbor == endWord:
39                            return diff + 1
40
41                        # If we haven't seen this word before, add to queue
42                        if neighbor not in visited:
43                            visited.add(neighbor)
44                            q.append(neighbor)
45            
46            # Increment the path length after exploring one full level
47            diff += 1
48
49        # If the queue is empty and we never hit endWord, no path exists
50        return 0