from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def find_subsequence(nums, seq, result):
            if len(seq) >= 2:
                result.append(seq)
            used = set([])
            for i in range(len(nums)):
                if not seq or nums[i] >= seq[-1]:
                    if nums[i] not in used:
                        find_subsequence(nums[i+1:], seq + [nums[i]], result)
                        used.add(nums[i])
        result = []
        find_subsequence(nums, [], result)
        return result