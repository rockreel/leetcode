from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def combinationSumImpl(candidates: List[int], target: int) -> List[List[int]]:
            result = []
            prev = None
            for i, c in enumerate(candidates):
                if c == prev:
                    continue
                if c == target:
                    result.append([c])
                elif c < target:
                    for r in combinationSumImpl(candidates[i+1:], target - c):
                        result.append([c] + r)
                prev = c
            return result
        candidates = sorted(candidates)
        return combinationSumImpl(candidates, target)