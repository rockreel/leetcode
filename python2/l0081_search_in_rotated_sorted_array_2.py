class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
            
        start, end = 0, len(nums) - 1
        while start <= end:
            middle = (start + end) / 2

            if nums[middle] == target:
                return True
                
            if nums[start] < nums[end]:
                # Regular sorted array.
                if nums[middle] < target:
                    start = middle + 1
                else:
                    end = middle - 1
            else:
                # Rotated sorted array.
                if nums[middle] > nums[start]:
                    if nums[middle] > target and target >= nums[start]:
                        end = middle - 1
                    else:
                        start = middle + 1
                elif nums[middle] < nums[start]:
                    if nums[middle] < target and target <= nums[end]:
                        start = middle + 1
                    else:
                        end = middle -1
                else:
                    start += 1
        return False

