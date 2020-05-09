from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def word_sig(word):
            sig = 0
            for c in word:
                mask = 1 << (ord(c) - ord('a'))
                sig = sig | mask
            return sig
                
        max_product = 0
        word_sigs = [(word_sig(w), len(w)) for w in words]
        for i in range(len(word_sigs)):
            for j in range(i+1, len(word_sigs)):
                if word_sigs[i][0] & word_sigs[j][0] == 0:
                    max_product = max(max_product, word_sigs[i][1] * word_sigs[j][1])
        return max_product
