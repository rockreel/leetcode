from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        existing = set()
        repeated = set()
        for i in range(len(s)-9):
            seq = s[i:i+10]
            if seq in existing:
                repeated.add(seq)
            else:
                existing.add(seq)
        return list(repeated)
