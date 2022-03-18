from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {}
        for i, l in enumerate(list1):
            index_map[l] = i
        min_idx_sum = len(list1) + len(list2)
        result = []
        for i, l in enumerate(list2):
            if l in index_map:
                idx_sum = index_map[l] + i
                if idx_sum < min_idx_sum:
                    min_idx_sum = idx_sum
                    result = [l]
                elif idx_sum == min_idx_sum:
                    result.append(l)
        return result