from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start, end = -1, len(arr)
        
        while start + 1 < end:
            middle = start + (end - start) // 2
            if arr[middle] == x:
                start, end = middle, middle + 1
                break
            elif arr[middle] > x:
                end = middle
            else:
                start = middle
        i = 0
        while i < k:
            if start < 0:
                end += 1
            elif end > len(arr) - 1:
                start -= 1
            else:
                if (x - arr[start]) <= (arr[end] - x):
                    start -= 1
                else:
                    end += 1
            i += 1
        return arr[start+1:end]