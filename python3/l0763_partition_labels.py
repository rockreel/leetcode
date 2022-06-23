from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        right_index_map = {}
        for i in range(len(s)-1, -1, -1):
            if s[i] not in right_index_map:
                right_index_map[s[i]] = i
                
        right = 0
        left = -1
        partitions = []
        for i in range(len(s)):
            right = max(right, right_index_map[s[i]])
            if i == right:
                partitions.append(right - left)
                left = right
        
        return partitions