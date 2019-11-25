# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i = 0
        while i < len(intervals):
            if newInterval.end < intervals[i].start:
                intervals.insert(i, newInterval)
                break
            elif newInterval.start > intervals[i].end:
                i += 1
            else:
                intervals[i].start = min(newInterval.start, intervals[i].start)
                intervals[i].end = max(newInterval.end, intervals[i].end)
                    
                while i + 1 < len(intervals) and intervals[i].end >= intervals[i+1].start:
                    intervals[i].end = max(intervals[i+1].end, intervals[i].end)
                    intervals.pop(i+1)
                break
        else:
            intervals.append(newInterval)
                    
        return intervals

