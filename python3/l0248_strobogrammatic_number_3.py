from typing import List

class Solution:

    def strobogrammaticInRange(self, low: str, high: str) -> int:
        # write your code here

        def generate_strobogrammatic(n: int, n_low: int, n_high: int, nums_in_range: List[str]):
            num_map = {
                '1': '1', '6': '9', '8': '8',
                '9': '6', '0': '0'
            }
            nums = []
            if n == 0:
                nums = ['']
            elif n == 1:
                nums = [k for k in num_map.keys() if k not in ['6', '9']]
            else:
                for num in generate_strobogrammatic(n-2, n_low, n_high, nums_in_range):
                    for k, v in num_map.items():
                        nums.append(k + num + v)
            if n_low <= n <= n_high:
                nums_in_range.extend(nums)
            return nums

        nums_in_range = []
        generate_strobogrammatic(len(high), len(low), len(high), nums_in_range)
        generate_strobogrammatic(len(high) - 1, len(low), len(high), nums_in_range)
        nums_filtered = []
        for n in nums_in_range:
            if len(n) > 1 and n[0] == '0':
                continue
            if len(n) == len(low) and n < low:
                continue
            elif len(n) == len(high) and n > high:
                continue
            nums_filtered.append(n)
        return len(nums_filtered)

