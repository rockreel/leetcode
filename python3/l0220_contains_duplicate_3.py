from collections import defaultdict
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        num_key_to_num_map = defaultdict(list)  # A list of numbers that map to the key.
        idx_to_num_key_map = dict()  # Number index to key the number maps to.
        for i, n in enumerate(nums):
            if t > 0:
                key = n // t
            else:
                key = n

            for num in num_key_to_num_map[key]:
                if abs(num - n) <= t:
                    return True
            for num in num_key_to_num_map[key-1]:
                if abs(num - n) <= t:
                    return True
            for num in num_key_to_num_map[key+1]:
                if abs(num - n) <= t:
                    return True

            # Add current number to the map.
            num_key_to_num_map[key].append(n)
            num_key_to_num_map[key-1].append(n)
            num_key_to_num_map[key+1].append(n)
            idx_to_num_key_map[i] = key

            # Pop numbers out of index range.
            if i >= k:
                prev_key = idx_to_num_key_map[i-k]
                num_key_to_num_map[prev_key].pop(0)
                num_key_to_num_map[prev_key-1].pop(0)
                num_key_to_num_map[prev_key+1].pop(0)

        return False