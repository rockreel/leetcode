class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        word_index_map = dict([(w, i) for i, w in enumerate(words)])
        result = set([])
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                if word[j:][::-1] in word_index_map and word_index_map[word[j:][::-1]] != i and word[:j] == word[:j][::-1]:
                    result.add((word_index_map[word[j:][::-1]], i))
                if word[:j][::-1] in word_index_map and word_index_map[word[:j][::-1]] != i and word[j:] == word[j:][::-1]:
                    result.add((i, word_index_map[word[:j][::-1]]))
        return [[r[0], r[1]] for r in result]

