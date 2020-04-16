from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        range_map = dict()
        max_n = max(nums)
        min_n = min(nums)
        ranges = []
        while num_set:
            n = num_set.pop()
            i = 1
            while n + i <= max_n:
                if n + i in num_set:
                    num_set.remove(n+i)
                else:
                    break
                i += 1
            j = 1
            while n - j >= min_n:
                if n - j in num_set:
                    num_set.remove(n-j)
                else:
                    break
                j += 1
            ranges.append((n-j+1, n+i-1))

        return max([e-s+1 for s, e in ranges])