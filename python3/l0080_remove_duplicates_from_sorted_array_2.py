class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup_count = 0
        i0, i1 = 0, 1
        while i1 < len(nums):
            if nums[i1] != nums[i0]:
                nums[i0+1], nums[i1] = nums[i1], nums[i0+1]
                i0 += 1
                dup_count = 0
            else:
                dup_count += 1
                if dup_count < 2:
                    nums[i0+1], nums[i1] = nums[i1], nums[i0+1]
                    i0 += 1
            i1 += 1
        return i0 + 1
