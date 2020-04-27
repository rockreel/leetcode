from collections import defaultdict

class WordDistance:

    """
    @param words: a list of words
    """
    def __init__(self, words):
        self._word_to_index = defaultdict(list)
        for i, word in enumerate(words):
            self._word_to_index[word].append(i)

    """
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortest(self, word1, word2):
        # Write your code here
        i, j = 0, 0
        dist = float('inf')
        l1 = self._word_to_index[word1]
        l2 = self._word_to_index[word2]
        while i < len(l1) and j < len(l2):
            dist = min(dist, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        while i < len(l1) :
            dist = min(dist, abs(l1[i] - l2[j]))
            i += 1
        while j < len(l2):
            dist = min(dist, abs(l1[i] - l2[j]))
            j += 1

        return dist
