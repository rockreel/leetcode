from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return arr
        greatest = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            current = arr[i]
            arr[i] = greatest
            if current > greatest:
                greatest = current
        return arr