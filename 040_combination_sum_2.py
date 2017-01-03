class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        result = []
        i = 0
        while i < len(candidates):
            c = candidates[i]
            if c == target:
                result.append([c])
            elif c < target:
                for r in self.combinationSum2(candidates[i+1:], target-c):
                    result.append([c] + r)
            while i < len(candidates) and candidates[i] == c:
                i += 1
        return result

