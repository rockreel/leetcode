class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
            
        start = 0
        end = len(nums) - 1
        result = -1
        
        while start <= end:
            middle = (start + end) / 2
            if nums[middle] == target:
                return middle
                
            if nums[start] < nums[end]:
                # Regular sorted array.
                if nums[middle] < target:
                    start = middle + 1
                else:
                    end = middle - 1
            else:
                # Rotated sorted array.
                if nums[middle] <= nums[end]:
                    if nums[middle] < target and target <= nums[end]:
                        start = middle + 1
                    else:
                        end = middle - 1
                else:
                    if nums[middle] > target and target >= nums[start]:
                        end = middle - 1
                    else:
                        start = middle + 1
                
        return result

