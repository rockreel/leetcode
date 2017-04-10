class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][1] + 1:
                ranges.append((n, n))
            else:
                ranges[-1] = (ranges[-1][0], n)
        return [str(r[0]) if r[0] == r[1] else '%s->%s' % r for r in ranges]
