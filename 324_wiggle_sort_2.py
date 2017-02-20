# O(nlogn) time with O(n) space.
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(list(nums), reverse=True)
        j = 0
        for i in range(1, len(nums), 2):
            nums[i] = sorted_nums[j]
            j += 1
        for i in range(0, len(nums), 2):
            nums[i] = sorted_nums[j]
            j += 1

