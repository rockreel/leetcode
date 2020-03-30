from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def combinationSumImpl(candidates: List[int], target: int) -> List[List[int]]:
            result = []
            for i, c in enumerate(candidates):
                if c == target:
                    result.append([c])
                elif c < target:
                    for r in combinationSumImpl(candidates[i:], target - c):
                        result.append([c] + r)
            return result
        
        return combinationSumImpl(candidates, target)