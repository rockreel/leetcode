from typing import List
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def word_adjacent(s1: str, s2: str) -> bool:
            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                if diff > 1:
                    return False
            return True

        # Initialize word graph.
        wordList.append(beginWord)
        word_graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                word_graph[word[:i] + '*' + word[i+1:]].append(word)

        # BFS to find minimum steps.
        queue = [(beginWord, 1)]
        visited = set([beginWord])
        while queue:
            word, length = queue.pop(0)
            for i in range(len(word)):
                for w in word_graph[word[:i] + '*' + word[i+1:]]:
                    if w == endWord:
                        return length + 1
                    if w not in visited:
                        queue.append((w, length + 1))
                        visited.add(w)

        return 0
