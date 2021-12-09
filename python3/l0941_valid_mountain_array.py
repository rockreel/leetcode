from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        if arr[1] <= arr[0]:
            return False

        go_up = True
        for i in range(2, len(arr)):
            if go_up:
                if arr[i] == arr[i-1]:
                    return False
                if arr[i] < arr[i-1]:
                    go_up = False
            else:
                if arr[i] >= arr[i-1]:
                    return False
        return not go_up
