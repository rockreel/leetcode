from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_map = Counter(magazine)
        for c in ransomNote:
            letter_map[c] -= 1
        for _, c in letter_map.items():
            if c < 0:
                return False
        return True
