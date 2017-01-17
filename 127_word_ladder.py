class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        def find_neighbors(word, word_set):
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == word[i]:
                        continue
                    neighbor = word[:i]+c+word[i+1:]
                    if neighbor in word_set:
                        yield neighbor
                    
        # BFS to find shortest path.
        wordList.add(endWord)
        wordList.add(beginWord)
        queue = [(beginWord, 1)]
        while queue:
            word, steps = queue.pop(0)
            if word == endWord:
                return steps
            if word not in wordList:
                continue
            wordList.remove(word)
            for neighbor in find_neighbors(word, wordList):
                queue.append((neighbor, steps+1))

        return 0

