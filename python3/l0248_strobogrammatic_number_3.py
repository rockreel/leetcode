from typing import List

class Solution:

    def strobogrammaticInRange(self, low: str, high: str) -> int:
        # write your code here

        def generate_strobogrammatic(n: int, low: str, high: str, result: List[int]):
            num_map = {
                '1': '1', '6': '9', '8': '8',
                '9': '6', '0': '0'
            }
            nums = []
            if n == 0:
                return ['']
            elif n == 1:
                nums = [k for k in num_map.keys() if k not in ['6', '9']]
            else:
                for num in generate_strobogrammatic(n-2, low, high, result):
                    for k, v in num_map.items():
                        nums.append(k + num + v)
            
            if len(low) <= n <= len(high):
                nums_valid = [n for n in nums if (len(n) == 1 or n[0] != '0')]
                if n == len(low):
                    nums_valid = [n for n in nums_valid if n >= low]
                if n == len(high):
                    nums_valid = [n for n in nums_valid if n <= high]
                result[0] += len(nums_valid)
            return nums

        result = [0]
        generate_strobogrammatic(len(high), low, high, result)
        generate_strobogrammatic(len(high) - 1, low, high, result)
        return result[0]

