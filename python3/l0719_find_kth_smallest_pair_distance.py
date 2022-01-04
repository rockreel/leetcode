from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess, nums, k):
            # If has k or more pairs with distance less than or equal to guess.
            left = 0
            count = 0
            for right, n in enumerate(nums):
                while n - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k
        
        nums.sort()
        start, end = 0, nums[-1] - nums[0]
        while start < end:
            middle = start + (end - start) // 2
            if possible(middle, nums, k):
                end = middle
            else:
                start = middle + 1
        return start