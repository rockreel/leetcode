# O(nlogn), sort solution.
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

# O(n), count solution.
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # Count citation by hindex.
        citation_by_hindex = [0] * (len(citations) + 1)
        for c in citations:
            if c < len(citation_by_hindex):
                citation_by_hindex[c] += 1
            else:
                citation_by_hindex[-1] += 1
        # Iterate from high to low find max hindex.
        num_total_citations = 0
        for h in range(len(citation_by_hindex)-1, -1, -1):
            num_total_citations += citation_by_hindex[h]
            if h <= num_total_citations:
                return h
        return 0
