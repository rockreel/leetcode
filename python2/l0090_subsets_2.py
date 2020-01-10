# Use a set to dedup.
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def subsets(nums):
            result = set([])
            for i, n in enumerate(nums):
                for s in subsets(nums[i+1:]):
                    result.add((n, ) + s)
            result.add(())
            return result
            
        return [list(s) for s in subsets(sorted(nums))]

# Manual dedup.
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def subsets(nums):
            if not nums:
                return [[]]
            # Find how many duplicates.    
            dup_count = 1
            while dup_count < len(nums) and nums[dup_count] == nums[dup_count-1]:
                dup_count += 1

            result = []
            for subset in subsets(nums[dup_count:]):
                for n in range(dup_count+1):
                    # Add [], [n], [n, n] .... to each subset excluding all n.
                    result.append([nums[0]]*n + subset)
            return result
        
        nums = sorted(nums)
        return subsets(nums)

