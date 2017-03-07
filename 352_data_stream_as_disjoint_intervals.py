# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import bisect
        self.summary = []  # List of tuple represents intervals.
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        interval = (val, val)
        if not self.summary:
            self.summary = [(val, val)]
            return
            
        i = bisect.bisect_left(self.summary, interval)
        if i == 0:
            # Insert at the beginning.
            if val < self.summary[0][0] - 1:
                self.summary.insert(0, (val, val))
            else:
                self.summary[0] = (min(val, self.summary[0][0]), self.summary[0][1])
        elif i == len(self.summary):
            # Insert at the end.
            if val > self.summary[-1][1] + 1:
                self.summary.append((val, val))
            else:
                self.summary[-1] = (self.summary[-1][0], max(val, self.summary[-1][1]))
        else:
            if val == self.summary[i-1][1] + 1 and val == self.summary[i][0] - 1:
                # Merge two interval together.
                self.summary[i-1] = (self.summary[i-1][0], self.summary[i][1])
                self.summary.pop(i)
            elif val <= self.summary[i-1][1] + 1:
                # Fall in previous interval.
                self.summary[i-1] = (self.summary[i-1][0], max(val, self.summary[i-1][1]))
            elif val >= self.summary[i][0] - 1:
                # Fall in next interval
                self.summary[i] = (min(val, self.summary[i][0]), self.summary[i][1])
            else:
                # Not connected to any intervals.
                self.summary.insert(i, (val, val))


    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        #return self.summary
        return [Interval(i[0], i[1]) for i in self.summary]
        

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()

