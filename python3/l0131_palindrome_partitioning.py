from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:    
        if len(s) == 0:
            return [[]]
                
        if len(s) == 1:
            return [[s]]
        
        partitions = []
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                for p in self.partition(s[i:]):
                    partitions.append([s[:i]] + p)

        return partitions