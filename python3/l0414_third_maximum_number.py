from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_nums = [None, None, None]
        for n in nums:
            if n == max_nums[0] or n == max_nums[1] or n == max_nums[2]:
                continue
            if max_nums[0] is None or n > max_nums[0]:
                max_nums[2] = max_nums[1]
                max_nums[1] = max_nums[0]
                max_nums[0] = n
            elif max_nums[1] is None or n > max_nums[1]:
                max_nums[2] = max_nums[1]
                max_nums[1] = n
            elif max_nums[2] is None or n > max_nums[2]:
                max_nums[2] = n
        
        return max_nums[2] if max_nums[2] is not None else max_nums[0]

    def thirdMaxHeap(self, nums: List[int]) -> int:
        import heapq
        max_nums = []
        max_num_set = set([])
        for n in nums:
            if n in max_num_set:
                continue
            if len(max_nums) < 3:
                heapq.heappush(max_nums, n)
                max_num_set.add(n)
            elif n > max_nums[0]:
                max_num_set.remove(max_nums[0])
                max_num_set.add(n)
                heapq.heappop(max_nums)
                heapq.heappush(max_nums, n)

        if len(max_nums) == 3:
            return max_nums[0]

        return max(max_nums)