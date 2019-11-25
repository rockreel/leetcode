class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        end_idx = 1
        dup_count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[end_idx-1]:
                if dup_count < 1:
                    dup_count += 1
                    nums[i], nums[end_idx] = nums[end_idx], nums[i]
                    end_idx += 1
            else:
                dup_count = 0
                nums[i], nums[end_idx] = nums[end_idx], nums[i]
                end_idx += 1
        return end_idx

