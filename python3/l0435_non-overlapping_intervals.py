from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals)
        count = 0
        pos = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < pos:
                if intervals[i][1] < pos:
                    pos = intervals[i][1]
                count += 1
            else:
                pos = intervals[i][1]
            
        return count
