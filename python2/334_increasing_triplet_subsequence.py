class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import sys
        s1 = sys.maxint  # arr[i]
        s2 = sys.maxint  # arr[j]
        for n in nums:
            if n > s2:
                return True
            if n > s1:
                s2 = n
            else:
                s1 = n
        return False

