import unittest

from l0249_group_shifted_strings import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(sorted([
                ['abc', 'bcd', 'xyz'],
                ['az', 'ba'],
                ['acef'],
                ['a', 'z'],
            ]),
            sorted(Solution().groupStrings(['abc', 'bcd', 'acef', 'xyz', 'az', 'ba', 'a', 'z'])))

