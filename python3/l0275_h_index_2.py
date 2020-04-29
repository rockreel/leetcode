from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = citations[::-1]
        start, end = 0, len(citations) - 1
        while start <= end:
            mid = (start + end) // 2
            h = mid + 1
            if h == citations[mid]:
                return h
            elif h > citations[mid]:
                end = mid - 1
            else:
                start = mid + 1
        
       
        return start

