from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def generate_combination(nums: List[int], k: int) -> List[List[int]]:
            if k == 1:
                return [[n] for n in nums]
            combinations = []
            for i, n in enumerate(nums[:len(nums)-k+1]):
                for c in generate_combination(nums[i+1:], k-1):
                    combinations.append([n]+c)
            return combinations

        nums = list(range(1, n+1))
        return generate_combination(nums, k)

    def combineIndex(self, n: int, k: int) -> List[List[int]]:
        def get_combination(start, n, k):
            if k == 0:
                return [[]]
            result = []
            for i in range(start, n):
                for c in get_combination(i+1, n, k-1):
                    result.append([i] + c)
            return result
        return get_combination(1, n+1, k)