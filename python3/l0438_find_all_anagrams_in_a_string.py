from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        letter_map = Counter(p)
        letter_mismatch = len(letter_map.keys())
        result = []
        
        for i in range(len(s)):
            letter_map[s[i]] -= 1
            if letter_map[s[i]] == 0:
                letter_mismatch -= 1
            elif letter_map[s[i]] == -1:
                letter_mismatch += 1
            j = i - len(p)  # Index to take out from window.
            if j >= 0:
                letter_map[s[j]] += 1
                if letter_map[s[j]] == 0:
                    letter_mismatch -= 1
                elif letter_map[s[j]] == 1:
                    letter_mismatch += 1
            if letter_mismatch == 0:
                result.append(j+1)
        return result  