from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def subsets(nums: List[int]) -> List[List[int]]:
            if not nums:
                return [[]]
            result = []
            # Find duplicates of first number.
            i = 0
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            
            # Skip duplicates to generate subset of next number.
            for s in subsets(nums[i+1:]):
                result.append(s)
                # Append duplicate numbers to subset.
                for j in range(i+1):
                    result.append([nums[0]]*(j+1)+s)
            return result

        nums = sorted(nums)
        return subsets(nums)