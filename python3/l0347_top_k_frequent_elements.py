from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        heap = []
        return [n for _, n in heapq.nlargest(k, [(c, n) for n, c in num_count.items()])]
