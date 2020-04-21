import unittest

from l0179_largest_number import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('210', Solution().largestNumber([10, 2]))
        self.assertEqual('9534330', Solution().largestNumber([3, 30, 34, 5, 9]))
