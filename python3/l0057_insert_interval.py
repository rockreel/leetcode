import bisect
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        pos = bisect.bisect_left(intervals, newInterval)
        intervals.insert(pos, newInterval)
        if pos > 0:
            pos = pos - 1
        while pos + 1 < len(intervals):
            if intervals[pos][1] >= intervals[pos+1][0]:
                intervals[pos][1] = max(intervals[pos+1][1], intervals[pos][1])
                intervals.pop(pos+1)
            else:
                pos += 1
        return intervals