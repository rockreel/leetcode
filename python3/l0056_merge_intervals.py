from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        merged = []
        for interval in intervals:
            if not merged:
                merged.append(interval)
                continue
            if interval[0] <= merged[-1][1] and interval[1] > merged[-1][1]:
                merged[-1][1] = interval[1]
            elif interval[0] > merged[-1][1]:
                merged.append(interval)
        return merged