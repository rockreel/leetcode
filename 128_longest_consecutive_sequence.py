class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        max_count = 0
        while num_set:
            for n in nums:
                start = n
                count = 0
                # Upper bound.
                while start in num_set:
                    count += 1
                    num_set.remove(start)
                    start += 1
                start = n - 1
                # Lower bound.
                while start in num_set:
                    count += 1
                    num_set.remove(start)
                    start -= 1
                
                max_count = max(max_count, count)
        return max_count

