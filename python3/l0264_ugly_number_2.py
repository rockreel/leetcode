class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2, i3, i5 = 0, 0, 0
        while len(nums) < n:
            if nums[i2]*2 <= nums[i3]*3 and nums[i2]*2 <= nums[i5]*5:
                n0 = nums[i2]*2
                i2 += 1
            elif nums[i3]*3 <= nums[i2]*2 and nums[i3]*3 <= nums[i5]*5:
                n0 = nums[i3]*3
                i3 += 1
            else:
                n0 = nums[i5]*5
                i5 += 1
            if n0 > nums[-1]:
                nums.append(n0)
        return nums[-1]
        
