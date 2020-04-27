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
            if word in (word1, word2):
                last_idx = word2_idx if word == word1 else word1_idx
                if last_idx is not None:
                    dist = min(dist, i - last_idx)
            if word == word1:
                word1_idx = i
            if word == word2:
                word2_idx = i
        return dist
