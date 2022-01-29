from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            while nums[i] != i:
                if nums[i] == len(nums):
                    break
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp
            i += 1
        for i, n in enumerate(nums):
            if n == len(nums):
                return i
        return len(nums)

    def missingNumberExtraSpace(self, nums: List[int]) -> int:
        found_nums = [0] * (len(nums) + 1)
        for n in nums:
            found_nums[n] = 1
        return found_nums.index(0)