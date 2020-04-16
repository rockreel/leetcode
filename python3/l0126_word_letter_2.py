from typing import List
from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        # Initialize word graph.
        if beginWord not in wordList:
            wordList.append(beginWord)
        word_graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                word_graph[word[:i] + '*' + word[i+1:]].append(word)

        # BFS to find minimum steps.
        min_length = len(wordList)
        length = 1
        ladders = []
        queue = [[beginWord]]
        # Visited set is updated per level so revisit on same node is allowed as long as
        # it is at the same level. This is to find all possible paths for a given length.
        visited_prev_level = set([beginWord]) 
        visited_all = set([beginWord])
        
        while queue:
            ladder = queue.pop(0)

            if len(ladder) > length:
                length = len(ladder)
                visited_prev_level.update(visited_all)

            if len(ladder) + 1 > min_length:
                break

            reach_end = False
            for i in range(len(ladder[-1])):
                for w in word_graph[ladder[-1][:i] + '*' + ladder[-1][i+1:]]:
                    if w == endWord:
                        min_length = len(ladder) + 1
                        ladders.append(ladder + [w])
                        reach_end = True
                        break
                    elif w not in visited_prev_level:
                        visited_all.add(w)
                        queue.append(ladder + [w])
                if reach_end:
                    break

        return ladders
