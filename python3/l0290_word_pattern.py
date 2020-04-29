class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        if len(pattern) != len(words):
            return False
        pattern_to_word = dict()
        word_to_pattern = dict()
        for p, w in zip(pattern, words):
            print(p, w)

            if p not in pattern_to_word and w not in word_to_pattern:
                pattern_to_word[p] = w
                word_to_pattern[w] = p
            else:
                if pattern_to_word.get(p) != w or word_to_pattern.get(w) != p:
                    return False
        return True