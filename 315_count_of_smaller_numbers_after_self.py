class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import bisect
        nums_after = []
        result = []
        for n in nums[::-1]:
            result.append(bisect.bisect_left(nums_after, n))
            nums_after.insert(result[-1], n)
        return result[::-1]

