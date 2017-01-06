# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted([(i.start, i.end) for i in intervals])
        merged_intervals = []
        i = 0
        while i < len(intervals):
            curr_inter = intervals[i]
            j = i + 1
            while j < len(intervals) and curr_inter[1] >= intervals[j][0]:
                curr_inter = (curr_inter[0], max(curr_inter[1], intervals[j][1]))
                j += 1
            merged_intervals.append(curr_inter)
            i = j

        return [Interval(i[0], i[1]) for i in merged_intervals]
                

