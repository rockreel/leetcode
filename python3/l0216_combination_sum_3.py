from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def combination_sum(nums: List[int], k: int, target: int):
            if target == 0:
                if k == 0:
                    return [[]]
                else:
                    return []
            
            combinations = []
            for i, n in enumerate(nums):
                if n > target:
                    continue
                for c in combination_sum(nums[i+1:], k-1, target-n):
                    combinations.append([n] + c)
            return combinations

        nums = [i for i in range(1, 10)]
        return combination_sum(nums, k, n)

    def combinationSum3SharedResult(self, k: int, n: int) -> List[List[int]]:
        def get_combination_sum(start, k, n, combination, result):
            if k == 0 and n ==0:
                result.append(combination)

            for i in range(start, 10):
                if n - i < 0:
                    continue
                get_combination_sum(i+1, k-1, n-i, combination+[i], result)
                
        result = []    
        get_combination_sum(1, k, n, [], result)
        return result
