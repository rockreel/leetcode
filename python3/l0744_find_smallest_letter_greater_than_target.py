from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, end = -1, len(letters) - 1
        while start < end:
            middle = start + (end - start) // 2 + 1
            if letters[middle] > target:
                end = middle - 1
            else:
                start = middle
        if start < len(letters) - 1:
            return letters[start+1]
        else:
            return letters[0]