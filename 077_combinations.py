class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def getCombination(nums, k):
            # Return combination has k elements using number from nums.
            if not nums:
                return []
            if k == 1:
                return [[n] for n in nums]
            result = []
            for i, n in enumerate(nums):
                for c in getCombination(nums[i+1:], k-1):
                    result.append([n] + c)
            return result
            
        nums = range(1, n+1)
        return getCombination(nums, k)

