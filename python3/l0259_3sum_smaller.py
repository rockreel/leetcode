class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def threeSumSmaller(self, nums, target):
        # Write your code here
        nums = sorted(nums)
        count = 0
        for i in range(len(nums)):
            target_2 = target - nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                while j <= k and nums[j] + nums[k] >= target_2:
                    k -= 1
                if k <= j:
                    break
                count += k - j
                j += 1
        return count
