class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortestDistance(self, words, word1, word2):
        # Write your code her
        word1_idx = None
        word2_idx = None
        dist = len(words) + 1
        for i, word in enumerate(words):
            if word == word1:
                if word2_idx is not None:
                    dist = min(dist, i - word2_idx)
                word1_idx = i
            if word == word2:
                if word1_idx is not None:
                    dist = min(dist, i - word1_idx)
                word2_idx = i
        return dist
