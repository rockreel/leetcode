# percentage: 7.96%
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                k, l = j + 1, len(nums) - 1
                # Two sum find target.
                while k < l:
                    if nums[k] + nums[l] == target - nums[i] - nums[j]:
                        result.append((nums[i], nums[j], nums[k], nums[l]))
                        while k + 1 < len(nums) and nums[k] == nums[k+1]:
                            k += 1
                        while l - 1 > 0 and nums[l] == nums[l-1]:
                            l -= 1
                        k += 1
                        l -= 1
                    elif nums[k] + nums[l] < target - nums[i] - nums[j]:
                        k += 1
                    else:
                        l -= 1
                # Increment j until no duplicate.        
                while j + 1 < len(nums) and nums[j] == nums[j+1]:
                    j += 1
                j += 1
            # Increment i until no duplicate. 
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            i += 1
            
        return result
