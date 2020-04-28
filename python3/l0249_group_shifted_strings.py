from collections import defaultdict
from typing import List

class Solution:

    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def calculate_key(s: str) -> str:
            if not s:
                return ''
            # Calculate signature key for each string.
            sig = []
            for c in s:
                k = (ord(c) - ord(s[0]) + 26) % 26
                sig.append(chr(k))
            return ''.join(sig)
        
        group_map = defaultdict(list)   
        for s in strings:
            group_map[calculate_key(s)].append(s)
        return list(group_map.values())
