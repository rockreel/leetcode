class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        for i, c in enumerate(candidates):
            if c == target:
                result.append([c])
            elif c < target:
                for r in self.combinationSum(candidates[i:], target - c):
                    result.append([c] + r)
        return result                
        
