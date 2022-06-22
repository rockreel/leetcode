from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i, j = 0, 0
        result = 0
        g = sorted(g)
        s = sorted(s)
        while i < len(g):
            while j < len(s) and s[j] < g[i]:
                j += 1
            if j < len(s):
                result += 1
                j += 1
                i += 1
            else:
                break
        return result