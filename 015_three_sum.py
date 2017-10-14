class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def twoSum(nums, target):
            i, j = 0, len(nums) - 1
            result = []
            while i < j:
                if nums[i] + nums[j] == target:
                    result.append([nums[i], nums[j]])
                    while i + 1 < len(nums) and nums[i+1] == nums[i]:
                        i += 1
                    while j - 1 >= 0 and nums[j-1] == nums[j]:
                        j -= 1
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
            return result    
        
        nums = sorted(nums)
        result = []
        i = 0
        while i < len(nums):
            result.extend([[nums[i]] + r for r in twoSum(nums[i+1:], -nums[i])])
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            i += 1
            
        return result
        