# One line hash map solution.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        return [k for k, v in Counter(nums).iteritems() if v != 3][0]

