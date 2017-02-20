class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = [(set(w), len(w)) for w in words]
        max_length = 0
        for i, (w1, len1) in enumerate(words):
            for w2, len2 in words[i+1:]:
                if w1 - w2 == w1:
                    max_length = max(max_length, len1*len2)
        return max_length

