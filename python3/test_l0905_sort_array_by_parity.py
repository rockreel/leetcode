import unittest

from l0905_sort_array_by_parity import Solution

def validate(nums):
    is_even = True
    for n in nums:
        if n % 2 != 0:
            is_even = False
        elif not is_even and n % 2 == 0:
            return False
    return True

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            True, 
            validate(Solution().sortArrayByParity([3, 1, 2, 4])))
        self.assertEqual(
            True, 
            validate(Solution().sortArrayByParity([0])))

        