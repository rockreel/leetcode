"""
Definition of Interval.
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        if len(intervals) <= 1:
            return True
        intervals = sorted(intervals, key=lambda x: x.start)
        last_end_time = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < last_end_time:
                return False
            last_end_time = interval.end
        return True
