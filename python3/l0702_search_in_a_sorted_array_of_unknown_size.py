from typing import List

class ArrayReader:
    
    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def get(self, i: int):
        if i >= 0 and i < len(self.nums):
            return self.nums[i]
        return 2147483647

class Solution:
    
    def search(self, reader: ArrayReader, target: int):
        end = 1
        while reader.get(end) < target:
            end = 2 * end
        start = end // 2
        
        while start <= end:
            middle = start + (end - start) // 2
            if reader.get(middle) == target:
                return middle
            if reader.get(middle) > target:
                end = middle - 1
            else:
                start = middle + 1
        
        return -1 
