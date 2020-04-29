class Solution:
    def hIndex(self, citations: List[int]) -> int:


        citations = sorted(citations, reverse=True)
        hmax = 0
        for i, c in enumerate(citations):
            h = i + 1
            if c >= h:
                hmax = h
        return hmax
