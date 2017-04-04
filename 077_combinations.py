class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def combination(nums, k):
            if k > len(nums):
                return []
            if k == 0:
                return [[]]
            result = []
            for i, n in enumerate(nums):
                for c in combination(nums[i+1:], k-1):
                    result.append([n]+c)
            return result
        nums = range(1, n+1)
        return combination(nums, k)
