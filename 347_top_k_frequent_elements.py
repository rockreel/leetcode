class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        num_counts = Counter(nums)
        top_k = sorted([(c, n) for n, c in num_counts.iteritems()], reverse=True)[:k]
        return [n for _, n in top_k]

