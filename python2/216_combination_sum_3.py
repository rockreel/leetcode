class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def combination_sum(k, target, nums):
            if k == 1:
                return [[n] for n in nums if n == target]
                
            result = []
            for i, n in enumerate(nums):
                if n >= target:
                    continue
                for r in combination_sum(k-1, target-n, nums[i+1:]):
                    result.append([n] + r)
            return result

        return combination_sum(k, n, range(1, 10))

