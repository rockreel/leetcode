from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x: x[1]) # Order by right edge.
        count = 0
        pos = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < pos:
                count += 1
            else:
                pos = intervals[i][1]
            
        return count
