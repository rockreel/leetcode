from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        buckets = [0] * 101
        cumulative_counts = [0] * 101
        for h in heights:
            buckets[h] += 1
        for i in range(1, len(buckets)):
            cumulative_counts[i] = cumulative_counts[i-1] + buckets[i]

        count = 0
        for i, h in enumerate(heights):
            num_shorter = cumulative_counts[h-1]
            num_shorter_or_equal = cumulative_counts[h]
            if i <= num_shorter - 1 or i > num_shorter_or_equal - 1:
                count += 1

        return count