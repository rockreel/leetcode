from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i, j = 0, 0
        while j < len(arr):
            if arr[i] == 0:
                j += 2
            else:
                j += 1
            i += 1
        i -= 1
        j -= 1

        if j == len(arr):
            # Last number to keep is a zero, manually shift back one more.
            arr[j-1] = 0
            j -= 2
            i -= 1
            
        while i >= 0:
            if arr[i] == 0:
                arr[j] = 0
                arr[j-1] = 0
                j -= 2
            else:
                arr[j] = arr[i]
                j -= 1
            i -= 1
        return
    
    def duplicateZeros1(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        def shiftLeft(arr: List[int], i: int) -> None:
            if i < 0 or i >= len(arr):
                return
            n = arr[i]
            while i + 1 < len(arr):
                t = arr[i+1]
                arr[i+1] = n
                n = t
                i += 1
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                shiftLeft(arr, i)
                i += 1
            i += 1
            
        return 