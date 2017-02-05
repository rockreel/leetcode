class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        if citations[0] >= len(citations):
            return len(citations)
        # Binary search to find largest h that satisfies
        # citations[i] <= h, h = len(citations)-1-i
        start, end = 0, len(citations)-1
        while start <= end:
            middle = (start + end) / 2
            h = len(citations) - 1 - middle
            if citations[middle] <= h:
                start = middle + 1
            else:
                end = middle - 1
        # h = len(citations) - 1 - (start - 1)
        return len(citations) - start

