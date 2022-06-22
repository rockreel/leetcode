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

    def combinationSum2GlobalResult(self, candidates: List[int], target: int) -> List[List[int]]:
        def combination(candidates, target, nums, result):
            if target == 0:
                result.append(nums)
                return
            if target < 0:
                return
            if not candidates:
                return
            for i, c in enumerate(candidates):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                combination(candidates[i+1:], target - c, [c] + nums, result)
            return
        result = []
        candidates = sorted(candidates)
        combination(candidates, target, [], result)
        return result