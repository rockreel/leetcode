from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        if not strs:
            return prefix
        s0 = strs[0]
        for i, c in enumerate(s0):
            for s in strs[1:]:
                if i >= len(s) or s[i] != c:
                    return prefix
            prefix = prefix + c
        return prefix