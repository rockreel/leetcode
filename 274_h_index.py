class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations, reverse=True)
        for i, c in enumerate(citations):
            if i + 1 > c:
                return i 
        return len(citations)

