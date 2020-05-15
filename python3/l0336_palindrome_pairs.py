from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_map = dict([(w, i) for i, w in enumerate(words)])
        result = set([])
        for i, word in enumerate(words):
            for j in range(len(word)+1):

                if word[:j] == word[:j][::-1]:
                    k = word_map.get(word[j:][::-1])
                    if k is not None and k != i:
                        result.add((k, i))
                if word[j:] == word[j:][::-1]:
                    k = word_map.get(word[:j][::-1])
                    if k is not None and k != i:
                        result.add((i, k))
        return [[r[0], r[1]] for r in result]

