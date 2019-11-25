class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(words) != len(pattern):
            return False
        pattern_to_word = {}
        word_set = set()  # To ensure reverse mapping is unique.
        for w, p in zip(words, pattern):
            if p in pattern_to_word:
                if w != pattern_to_word[p]:
                    return False
            else:
                if w not in word_set:
                    pattern_to_word[p] = w
                    word_set.add(w)
                else:
                    return False
        return True

