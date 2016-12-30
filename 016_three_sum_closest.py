# percentage: 49.05%
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        max_diff = None
        nums = sorted(nums)
        for i, n in enumerate(nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if target == n + nums[j] + nums[k]:
                    return target
                else:
                    if not max_diff or abs(target - (n + nums[j] + nums[k])) < abs(max_diff):
                        max_diff = target - (n + nums[j] + nums[k])
                    if nums[j] + nums[k] < target - n:
                        j += 1
                    else:
                        k -= 1
        return target - max_diff
