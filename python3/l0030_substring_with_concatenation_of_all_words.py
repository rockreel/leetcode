from typing import List
from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []

        index_to_word = dict()
        word_count = defaultdict(int)
        word_len = len(words[0])
        result = []

        for w in words:
            word_count[w] += 1

        for i in range(len(s)-word_len+1):
            if s[i:i+word_len] in word_count.keys():
                index_to_word[i] = s[i:i+word_len]
        
        for i in range(len(s)-word_len+1):
            visited_count = dict(word_count)
            num_match = 0
            for j in range(i, len(s)-word_len+1, word_len):
                if j not in index_to_word:
                    break
                if visited_count[index_to_word[j]] == 0:
                    break
                visited_count[index_to_word[j]] -= 1
                num_match += 1
                if num_match == len(words):
                    result.append(i)
                    break

        return result